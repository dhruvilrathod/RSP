import networkx as netx

text1 = """029A
980A
179A
456A
379A"""


text = """539A
964A
803A
149A
789A"""


directions = {
    (-1, 0): "^",
    (1, 0): "v",
    (0, -1): "<",
    (0, 1): ">",
}

numeric_keypad = netx.Graph()
numeric_positions = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

for key, (x, y) in numeric_positions.items():
    for neighbor, (nx, ny) in numeric_positions.items():
        if abs(x - nx) + abs(y - ny) == 1:
            numeric_keypad.add_edge(key, neighbor)

directional_keypad = netx.Graph()
directional_position = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

for key, (x, y) in directional_position.items():
    for neighbor, (nx, ny) in directional_position.items():
        if abs(x - nx) + abs(y - ny) == 1:
            directional_keypad.add_edge(key, neighbor)




def get_shortest_path(keypad, positions, start, code):
    path = []
    res = []
    current = start
    for char in code:
        moves = netx.shortest_path(keypad, current, char)
        path.extend(moves[1:])
        for i in range(len(moves)-1):
            move = (positions[moves[i+1]][0] - positions[moves[i]][0], positions[moves[i+1]][1] - positions[moves[i]][1])
            res.append(directions[move])
        res.append("A")
        current = char
    return "".join(res)


def get_all_shortest_paths(keypad, positions, start, code):
    all_paths = []
    current = start

    for char in code:
        shortest_paths = list(netx.all_shortest_paths(keypad, current, char))
        char_paths = []

        for path in shortest_paths:
            res = []
            for i in range(len(path) - 1):
                move = (
                    positions[path[i + 1]][0] - positions[path[i]][0],
                    positions[path[i + 1]][1] - positions[path[i]][1],
                )
                res.append(directions[move])
            res.append("A")
            char_paths.append("".join(res))
        
        if not all_paths:
            all_paths = char_paths
        else:
            new_paths = []
            for prev_path in all_paths:
                for char_path in char_paths:
                    new_paths.append(prev_path + char_path)
            all_paths = new_paths

        current = char

    return all_paths



def score_path(path, parent_positions, parent_start):
    score = 0
    current = parent_start
    transitions = 0
    for i in range(len(path)):
        if i > 0 and path[i] != path[i - 1]:
            transitions += 1  # Count transitions between different keys

        # Calculate the movement cost in the parent keypad
        if path[i] in parent_positions:
            target = parent_positions[path[i]]
            score += abs(current[0] - target[0]) + abs(current[1] - target[1])
            current = target

    return score + transitions


def find_shortest_path(code):
    moves1 = get_all_shortest_paths(numeric_keypad, numeric_positions, "A", code)
    moves1 = set(moves1)
    
    scored_moves1 = sorted(
        moves1,
        key=lambda m: score_path(m, directional_position, directional_position["A"])
    )

    moves2 = set()
    for m1 in scored_moves1[:5]:
        tempm2 = get_all_shortest_paths(directional_keypad, directional_position, "A", m1)
        tempm2 = set(tempm2)
        moves2 = moves2.union(tempm2)

    scored_moves2 = sorted(
        moves2,
        key=lambda m: score_path(m, directional_position, directional_position["A"])
    )

    moves3 = set()
    for m2 in scored_moves2[:5]:
        tempm3 = get_all_shortest_paths(directional_keypad, directional_position, "A", m2)
        tempm3 = set(tempm3)
        moves3 = moves3.union(tempm3)

    shortest_move = float('inf')
    for m3 in moves3:
        if len(m3) < shortest_move:
            shortest_move = len(m3)
    return shortest_move





cache = {}

def find_path_length_2(sequence, level_keypads, level=0, max_level=2):

    seq_str = "".join(sequence)
    if (seq_str, level) in cache:
        return cache[(seq_str, level)]

    keypad = level_keypads[level]
    positions = numeric_positions if level == 0 else directional_position
    sequence = ["A"] + sequence

    total_length = 0
    for i in range(len(sequence) - 1):
        start, end = sequence[i:i + 2]
        paths = get_all_shortest_paths(keypad, positions, start, end)

        scored_paths = sorted(
            paths,
            key=lambda path: score_path(path, directional_position, directional_position["A"])
        )

        min_length = float('inf')
        for path in scored_paths[:5]:
            if level < max_level:
                path_length = find_path_length_2(list(path), level_keypads, level + 1, max_level)
            else:
                path_length = len(path)

            if path_length < min_length:
                min_length = path_length

        total_length += min_length

    cache[(seq_str, level)] = total_length
    return total_length




def get_all_codes_paths(text):
    codes = text.split("\n")
    code_map = {}
    for c in codes:
        p = find_shortest_path(c)
        code_map[int(c[:-1])] = p
    
    return code_map


def get_all_codes_paths_2(text, max_level):
    level_keypads = {
        0: numeric_keypad,
        **{i: directional_keypad for i in range(1, max_level+1)}
    }
    codes = text.strip().split("\n")
    code_map = {}
    for c in codes:
        numeric_part = int(c[:-1])
        sequence = list(c)
        p = find_path_length_2(sequence, level_keypads, max_level=max_level)
        code_map[numeric_part] = p
    
    return code_map

def calculate_complexity(text):
    code_map = get_all_codes_paths(text)
    ans = 0
    for c in code_map:
        temp = c*code_map[c]
        ans += temp
    return ans


def calculate_complexity_2(text, max_level):

    code_map = get_all_codes_paths_2(text, max_level)
    total_complexity = 0
    for code, path_length in code_map.items():
        complexity = code * path_length
        total_complexity += complexity
    return total_complexity



ans1 = calculate_complexity(text)
print("answer:", ans1)


ans2 = calculate_complexity_2(text, 25)
print("answer:", ans2)
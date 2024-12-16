from collections import deque


text1 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

text2="""0123
1234
8765
9876"""

text = """901403454308767601987430010102103430787676
812312567219458912376541023411212321096787
765403498012307433489432196520303234585898
012354321087216524570343787434454100674301
985467891096987019601234378976569981001210
876654102345106508710765234789678972343454
798783287765278710789820105678710169858763
687690196894369821890112344589801258769012
501543285210152152721201453078987340150103
432457894101043043630328762101456498201232
870326543232032154549419234652343567398341
961210012343129069608500165765432985437650
054301456953238778217671876893211076126789
123012387869345632347889956544509089005491
128723498778734101256970987832678179012310
039614595654187214378921078981083238768723
340507680343096785561434563470198740059654
651408971252125896450001412563267651145098
762310564561034587321112303214107892230127
891023453478987878543203474905896543451936
678921962101216969458914985876708712767845
567630879870305456367325676765219603856696
654544567765412343210232110894334564943787
783203498894301210321143029889123765830654
890112985435213456787054334778010894321003
901209876120102365098765245667654784321212
892100125009871074109670123454743065210012
763119834312568983232189812303892178756763
654098701233457654983074505412789109349854
120145610145012523474563676545630201201340
034234543296543210565012985654321347652201
543007665487012365034876501745610458943102
632118978329110874128989432891234367812983
789327659418723923567876541010765298103894
879454341507654010430765430199804105412765
988761030676589012321650321783219876545630
896902321585438543456761230654323401454321
787813490492127654349854345013210562367212
076524582341013434234981016724505678498101
123433671034565521187832109834694989654342
589652180123877610096543258943783878701233
676543091012988987101234567652102107212344"""


def parse_input(input_map):
    return [list(map(int, line.strip())) for line in input_map.strip().split("\n")]

def find_trailheads(map_data):
    trailheads = []
    for r, row in enumerate(map_data):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_step(map_data, current, next_pos):
    rows, cols = len(map_data), len(map_data[0])
    r, c = next_pos
    if 0 <= r < rows and 0 <= c < cols:
        return map_data[next_pos[0]][next_pos[1]] == map_data[current[0]][current[1]] + 1
    return False

def calculate_trailhead_score(map_data, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = deque([start])
    reachable_nines = set()

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if map_data[current[0]][current[1]] == 9:
            reachable_nines.add(current)

        for dr, dc in directions:
            next_pos = (current[0] + dr, current[1] + dc)
            if is_valid_step(map_data, current, next_pos) and next_pos not in visited:
                queue.append(next_pos)

    return len(reachable_nines)

def calculate_total_score(text):
    map_data = parse_input(text)
    trailheads = find_trailheads(map_data)
    total_score = 0

    for trailhead in trailheads:
        total_score += calculate_trailhead_score(map_data, trailhead)

    return total_score

def explore_all_trail_paths(map_data, current, visited):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(map_data), len(map_data[0])
    r, c = current

    if map_data[r][c] == 9:
        return 1

    trail_count = 0
    visited.add(current)

    for dr, dc in directions:
        next_pos = (r + dr, c + dc)
        if (
            0 <= next_pos[0] < rows and 
            0 <= next_pos[1] < cols and 
            next_pos not in visited and 
            map_data[next_pos[0]][next_pos[1]] == map_data[r][c] + 1
        ):
            trail_count += explore_all_trail_paths(map_data, next_pos, visited)

    visited.remove(current)
    return trail_count


def calculate_total_ratings(text):
    map_data = parse_input(text)
    trailheads = find_trailheads(map_data)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += explore_all_trail_paths(map_data, trailhead, set())

    return total_rating



count = calculate_total_score(text)
print("Total Score:", count)



count1 = calculate_total_ratings(text)
print("Total rating:", count1)
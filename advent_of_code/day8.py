from collections import defaultdict

text1 = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


text = """...........6.b....................................
........6................8........................
..Y.......................................o.......
....V...j............B.............c..............
............8.........X.......L...................
.....j..v6.......3.L..................c...........
..Mj.....p3.......b........Z....................J.
..........M...X...................................
V..............v......p.........Z.........c.......
..............3...................................
.......V......U3.............c....................
..........b..v.M.U8...............................
..........j........8.....................J........
..........Y......q........LH..Z...D...........y...
..2Y........PX......6..................BQ.........
...0.Y...............XP...........w...............
.........U.......2...............oH.y.............
0..............9........U.........................
...........P..............W.......z...Oy..........
...................t...p.W..o.............Q.......
.....S.................t.....Q....B...............
S.k..................V..W...p.......H...O......m..
....S.h................W.......................O..
..h..P.2.............Z.............J..............
.........k.......5v.......q...t.s.................
.....Q.....h..........................J...B.......
........0.........l...............................
.S................................................
.............................M....................
2..................e.....o.....y..................
................k.................................
......4......k....t...s.q.........................
.4.......................q........................
.......................z....E.....................
.............0.....d..............................
7..........D........z.............................
.......D..5......7..9.............................
......5..................E........................
D..............K......d..9E..........w.....1..C...
.......K..x.........d....s...........l............
........7......................u...C..............
..K........x..............9..C...u................
4..............s.........................l...T..w.
.......5.....7..................m......T......1...
...........................E...z.m................
......................................u...C.......
.............................em...................
..............................................T...
....................x.......................e.....
.............................1e....w....l........."""

def parse_text(text):
    return text.split("\n")

def find_sources(text):
    text = parse_text(text)
    sources = defaultdict(list)
    for t in range(len(text)):
        for j in range(len(text[t])):
            if text[t][j] != ".":
                sources[text[t][j]].append((t, j))

    # print("all sources:", len(sources.keys()), "::",sources)
    return sources

def find_all_pairs(sources):
    pairs= {}
    for s in sources:
        pairs[s] = []
        for i in range(len(sources[s])-1):
            for j in range(i+1, len(sources[s])):
                pairs[s].append((sources[s][i], sources[s][j]))
    # print("all pairs: ", len(pairs.keys()), "::", pairs)
    return pairs

def flatten_sources(sources):
    srs = set()
    for s in sources:
        for i in range(len(sources[s])):
            srs.add(sources[s][i])

    # print("flatten sources: ", len(srs), "::", srs)
    return srs

def flatten_pairs(pairs):
    prs = set()
    for s in pairs:
        for i in range(len(pairs[s])):
            prs.add(pairs[s][i])

    # print("flatten pairs: ", len(prs), "::", prs)
    return prs

def find_antinode_position(pair, m, n):

    absoluteX = abs(pair[0][0] - pair[1][0])
    absoluteY = abs(pair[0][1] - pair[1][1])

    left = pair[0] if pair[0][0] < pair[1][0] else pair[1]
    right = pair[0] if pair[0][0] > pair[1][0] else pair[1]
    top = pair[0] if pair[0][1] < pair[1][1] else pair[1]
    bottom = pair[0] if pair[0][1] > pair[1][1] else pair[1]

    available_pos = set()

    if top == left:
        tempX1 = left[0] - absoluteX
        tempY1 = top[1] - absoluteY
        if tempY1 >= 0 and tempY1 < n and tempX1 >= 0 and tempX1 < m:
            available_pos.add((tempX1, tempY1))

        tempX2 = right[0] + absoluteX
        tempY2 = bottom[1] + absoluteY
        if tempY2 >= 0 and tempY2 < n and tempX2 >= 0 and tempX2 < m:
            available_pos.add((tempX2, tempY2))

    elif bottom == left:
        tempX3 = left[0] - absoluteX
        tempY3 = bottom[1] + absoluteY
        if tempY3 >= 0 and tempY3 < n and tempX3 >= 0 and tempX3 < m:
            available_pos.add((tempX3, tempY3))

        tempX4 = right[0] + absoluteX
        tempY4 = top[1] - absoluteY
        if tempY4 >= 0 and tempY4 < n and tempX4 >= 0 and tempX4 < m:
            available_pos.add((tempX4, tempY4))

    return available_pos

def find_all_antinodes(all_pairs, m, n):
    all_antinodes = set()
    for p in all_pairs:
        for a in find_antinode_position(p,m,n):
            all_antinodes.add(a)
    return all_antinodes

def count_antinodes(text):
    m,n = len(text.split("\n")), len(text.split("\n")[0])
    sources = find_sources(text)
    pairs = find_all_pairs(sources)
    f_sources = flatten_sources(sources)
    f_pairs = flatten_pairs(pairs)

    all_antinodes = find_all_antinodes(f_pairs,m,n)
    return len(all_antinodes)

def count_extended_antinodes(text):
    m,n = len(text.split("\n")), len(text.split("\n")[0])
    sources = find_sources(text)
    antinodes = set()
    for nodes in sources.values():
        if len(nodes) > 1:
            antinodes.update(set(nodes))
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                n1, n2 = nodes[i], nodes[j]
                xd, yd = n1[0] - n2[0], n1[1] - n2[1]

                x, y = xd, yd
                while 0 <= n1[0] + x < m and 0 <= n1[1] + y < n:
                    antinodes.add((n1[0] + x, n1[1] + y))
                    x += xd
                    y += yd

                x, y = xd, yd
                while 0 <= n2[0] - x < m and 0 <= n2[1] - y < n:
                    antinodes.add((n2[0] - x, n2[1] - y))
                    x += xd
                    y += yd

    return len(antinodes)

count = count_antinodes(text)
print("total:", count)

counte = count_extended_antinodes(text)
print("extended total:", counte)

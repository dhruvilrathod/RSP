from collections import deque


text1 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

text2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

text = """##################################################
#O..OOOO......#...O.#O..........OOO..O#.O..OO..###
#...O#...#...O.O...O.O........#OO...O.#O..O.O..O.#
#..O.......#O..OO.#..O..O...O....O#O.O.....O.....#
#O...O.O...O.O#.O..O....O..#OOO......#O......#.O.#
#O........O.#.#....OO............OO...O..O.......#
#..O.OO.OOOO.O.....OO....#OO....O.........#...#..#
#.....O........O....#....#OOO.O..................#
#...O...#O#.O.......O.O.OO.##...O.OO.O.....O...#.#
#OO.O#O....O..O....#O..OO....O.O..#OO.#O....OO.#.#
#O......#..O..OO#..OOO...O.#OOO...O......O.O..O..#
#.#....O.........OO.OO......O#O#..O#O......O...O.#
#O.#....O.OOO.#O.......O....O.OO...#..#...O......#
#O.....OOO.#....O.OO.#O.O................O.OO...##
#..O.#......O#OO...#...O.....O##..O..#..O...OO...#
##.O.O#.O.OO..O.....OO...##.....O.O.......#O...###
##..#......O.O#.O.O.O....O#OOO...O.#O...........O#
#O..........O...........O...O.#......O..O..O.O#O.#
#.......O#.O.O.O....O.....O.OO..O.OO....O.#..O.OO#
#O...OO.#..OOOO.#.................#.O.OO.O......O#
#.OOOO.#..OO...O.......#.O....O.....O.O.O....O...#
#.OO..OOOO....O....O....#...O..O..#...O.O.O#O.OO.#
#......OO........O.OO..O......O..OO........OO...O#
#.O.O.O.OO.OOO.O...OO.....#....O.....O.O.OOOO.OO.#
#O#.....O#....O.#....O..@OO......#..#..O.........#
#OO.OO.O...##O..OOO.O.#....O....OOO...O..O..#...O#
#.O..O.O..O....O.O..#..#..#.OO.#.OO.#.#O.......O.#
#...#..OO.O.........OO.........OO.OOO.O.....O.#.O#
#...........OO.OO#..OOO..#O.OO.....O...#O.OOO.O#O#
#.#O....O..O..#.....O.#.O..O........O..O...OO.#..#
#....O.OOOO......OO......OO..#...O.O...O......O..#
#...O..O.O.....O#..O..O.......OOOO.......O#...O..#
#....#...O.....O.O.O...O...............OOOO..#.O.#
#....OOO......#OOOO.O.#.O......O.O..#O.O#.....#..#
#O.OO.O.O.........OO#.......##........O#OOO...O..#
#..O.O#O#....#...#......O......#O...O....O....#.O#
#.O...OO.......O..O......OO......#..........O.#..#
#......O.O.O#O.#O#..O.O.OOO..O...O...#.O.O...O...#
#O...O.....O.#O.......OOO.#...O...O...O....OO..O.#
#..#.#.....OO.OOO.O.O#.O.....O...O..O..O..O......#
#......O..........O....#...O.O............O.#...O#
#.#O..OO.....O.O#OO.OO.OOO....O.......O........OO#
#....O#OO......OO#.O..O..O...O..OO...O..O..O..#.O#
#OOO..O..#.OO......O.O........#.O...O#.....O.....#
#..O.....#O....#.O...O.O#....O..O..O...O..O.O.O.O#
#..O#O.O#O...O.....#............O#.OOOO.O....OO..#
#..#.#O.O.....O...OO...O.O..#.#O...#.....#..O....#
#..OO..O.O..O.O.O.O.#.O...OOOO.O.....O.O##OO.O.#.#
#...OO.O..O..O......O.##......#OO.....O.O.OO.O.O.#
##################################################

^^^>^v<<>><>vv<><v^>>>^vv>^v>^>>>^<v>>^<^>^^>v>>>v<^>v<^vv>vvv^<<^<>v^^^<^^<>^<>^v^>v<<vv><v<<><v^<^<v<<v^vv<><v><^v><^v<^>>vv>>><v^><^>^^>v<v<<v^>^>^vv<^<^>^^v^<>v>v<^vv<>vv><>>v>^<v>v<^^^>v^^^<<vv<^^v<v^>v<^<<^>><>^v<v>><<<<v>v<v^<^v><vv<v>^<><^v>^^^v><<>vv>v<<<^v<^v<<>><^^v>^v<^^<><<v>^>><vv>v^vv><<v^^^<>>v^<<<v>><>><<<^><vv>^v>>>><vv<vv<>^^^<v^^^<v>v<<<v>^<><v^><><^><v<<<>^<>>^vv^<^<>><>^<<v>v<vv>><<>^vv^v<<><<v<^><v^vv^^<^>^vv<><v^^vv>^^><><>>^^<^>^^v>v>^v<^v^<^<^>v<v^^v>>v^<v^^^>vvvvv<v<^v<><<<vvv<<<>>^^^v>^>>v>><><>>>>>>vv^^<>v<<v<<^<><><>>>v^^<<<>vv>v<v^^<>^^<^<v<<v<<^><>>^>vv^v<><v<v<v>>v>^^vvv<v>v^^v<vv<^v^^<>>v^<v<<>v<<<><^vv<^^><>^v^>><^^v^^^v<^>vv<^v^>^<v<<v<<>^vv><^<<<<v><<<>^v<>>>>v<^^v^^v><^v^>><>^>>><v^>^^v^^<<vv>><v>^v>><vv<<v<v<>^>>>>v><<>><v<vv<v^^v>vv>^^^^><^><<^^vv^<<><^<^v^<<>>^^^<<^>>>v<>^<>v^v<>^^<^><<<<>v^<<<<><>^<>><<>>^^v>^>v<>><>^vv<<v<<<<v^>v<^v<<>^>^<<vvv<<v<>><^>v>^>^<<<>v^^>>v^v<<^<>>v><<>v^>v^^^<^^>^^>^>><^<<<<v^v<^<v^v^<<v^^v^^<^<>v<<^^^^vv^<v>v>>^>vv
<^<^^vv^^<<<><^<^^<^<v>v>v><<^<v><v^v><v^>v><>v><><><>>v<^^><^><><<><^^<vvvvv^><^^^v>vvv<<<<v^v^vvv<v<<v><<<^v^<<<^v<vv>v>v<>><>>><^^v<^^v<><<>^v>><>v^^<v>><>v<>>vv>^v<^vv>>v^>^>v^v^v<^>v><^v^<>^^<>^>v<^v^v<>>>^>>>v^v<>^<>v<v^vv>>vvvv<^<>v<<vv<v^v^<vv^<<^<^<><v>><>>^>^v>^v>vv<^<vv^<><vv<v^^>v><<<^v><<^>v><<v>>^vvvvv<v<^>^><>>>v^v>>^<^v<<<<>^vvv<>v>^>>^<>><^v^^>vv<<v^^>v<^<>>>^>>><^<>^^><>vv^<v>><><>^vv><<^v>v^><>^>^<><^vv^>^<<^<><v>vv<<v<>^<<^<v<^^v<^v^<<^<<^^v>>^<vvv^v^v><>v<v<<v>v^>v<>v<><^^<<^<v<vv^>v<<v^<>^<^v>^v<^v<^v<^vv<^v>v>>vv^^^v<<<<^>v^v<<vv^><^vv>v>^<v<^^^<<>^>^^vvvvv^>^<^>v^>>v<^vv><<>>>v><>v<^>^>>^v>^>v^^<^^v<^<<^><<v><vv><v^v^>^v>v>>>><<v<>v>^><<^>^v<^vv<<^^v>><^>^>v^<vvv>v><<>^v<^v^>vvv^<<^v<>>vvv<^><<>v<<^^^^<v>v<vvv^v>^<vv<<<vv><v>vv>v^<^><^><v<>vv^>^vv>>v>v>><^^<v<>>><>^<>v>>vv^v>^v^>^>v^^^v>^v><^>>^vv<vvv>>v<^^^<><^><>>><v^><<<^v^^^^<>v^<vv<<<v^^^<>^<v<^<v<vv>v<<>v^>>>^><^^>>>v<<>^<vv>^^^^<v>^<v^v<<>><^>>>^v^<vv>>v<^>v^><>>^<<>>^<>^vv<<vv>^>^>^^vv<>^v<v<>>v<v><<v^<>
<>vvv^v>>>><^v<v>><v>v^v^^>>vv><>v^^^^v<v>^<<<>^>>><^^<>^<><^>vv><vv>><^<v<^v<v^^^^>v><<v^v^>^v>><<^^<v<^v<>^>^<>>>>vv>^^<v<>v^v^<>>>vv^>vv<<>v<^<<^^v^v><<>^v^v>v^^>vv^v^^^vv<^<^^><<>v<^<v><>v^<^<<^v^>><<^^^<vv><<v>>^<^^<<v<v>>v^vv<>^>^>><<>^vvv^<^v<>>v<>>^<^<<v>v^>vv>vv>v>>^>^<^>^vvv^<<v^^v^<^<><v^>^<^>v^v>^<<^><>v>^^v><^^^><<><^^v^^v>v<>>vvvvv>v>><<>>>vv<^^<v<^>>v<vv<^>v<^vv<^<v^^><^^^<^<<<^vv^vv>v><v>^^^>v^^>^>v<v^<<^<^^<^v>>>>>v^<^^^>>>>vv<><<>>v^v>vv^v>v><>v^>>^^^<<><v>>><^^<v<^v>^>><^>^v<>><v<^^^v<^^>^vv>><^v>v>>>v>^^^><<^>v<^<v><<v<^>v>^>^vvvv^<^vv<^<<^>^vvvv><><v><v<^><vvvv<><^<v>>v^^>v^^>^v<>^<>vvv<<>^><v<<v>v><^><v<>vv<><^v<^<v>v^vv<v^vv<v<<vv>>>v<v>^>vv>>^^^v<v<vv>^><><>^>>><^<v<v^^^vv<v><<v^^v^^^<^v><<><vv<^>><^^<^<v>><<vv>>^^<><>v<<^>vv^v<v<<>vv>>><<^<^v^vvvv<vv<^><vv<<>>><>^^v<>^^>^<>>>^<v<<^v^vv><<v><v<<<vv<^v<<>^^>>><>>>><<^>vv<vv><<>^>>v>>v><v>><<^<v<>vv<^v>>>^^^v^>vv^>>^vvv^^v<><<>>v^v>^<<>>vv<<<v>>^<^>v<<<<vv>v^<v>^>><<^>v^v<<^^v<<<^>v<^^<^v<^>>v<v^><^^>vv>vvv^>^^<><
^<^>v>>v^vv<>vv<vvv^v^v^><><vv<>>>>>>^>><><vvv<v^^^v>>v^^vv<^>^>v<^>^<^^v>>^>^><<<^>>^v>>><<<<^^v<<>v^><v^v>>><<<><<>vv<^v<<v^^vv<^<vv^v^v^^<^<^<>^<<v>^^>^>^>>>vv>vv^^vv^^^v^>^<v>>vv><^<^<>><<^v>>^^^<>>><v^v^v<v>v>>^>>v><<vvv<^<>>><><>v<<^v<^>v>>vv<^v<vv>vv>v<^>vv<<v^>v^<>^<v<^v^^v^^<<<v^<><v<<vv><^vv<<><v<^v^>^v>>><^<>^v^^<<v>^v<^^v>vv<><><v>vv^<<<><^>><v>^^>^vvv^<>vvv^^>>><<>><v^v><<>>v>v><v^^><>v^>^v<<v<v^v>^<><v<v<^><>v^^<^vv>>^vvv<^>^>v>>>^^vvv>^^vvv>^^>v^vv^<<^^>^><v<<v^>>^<^>^v><<^^v^vv><v<v<<v<<^>^>^^^<<^<>>v>v>^^<vvv^^<>v><>^v>>>>vv>>^^^>vv><^^<v<<v>vv>v^vvv^<v>^^^v>><<^^<<^<>v^vv<v<^<vv<<^^>><><v>^v^><>^^<><><v^^^>vvv^v^<>^<><>v^>>><>^>>>><<vvv<v^v><^><>>^<vv>^<^<<v^^^<^v<v>>>vv<>>>>v^>v<>^><><<v<<<<>>v<v>vv<^>>v^^v<<v<^^<><^v<^<v<<<><^v<vvvv^<>^>>v^<><>^^<v><v<>><>>><v<<<><^vvvv<^v>><v<^v>^vvv<v<>vvv>^<<<>v>vv^^v><<vv^<>v>v^v>vv>vv>v>^>>>>><v><^>v>>vv<<v^^>>^^^v<<<^^<^>^<>^^^^^<v<>>^^<v^^v<>v<v^<^<^><^^^^>v>>^<<^vv<>v<^>>v>>vv<><>v^<vv<^^>v<v^<^<>>^>^^<>vv>>>^^vv<<^v>v^v<<v<
^v<^<>^<<>v<<><^<vv^v>>vv>^^^^^^vvvvv<>^>vvv^<<><>>^<>vv^<vv<v^^>^<^<v<<^vv^^^>^<><<v^>>^>>v<^vv^^<v^^^>v^<v<^<^vv>^vv<^^<v>>^<v^^>^>><vv^^v><v><v>v^<>>^v^<<^<>vv>>v<v>>v<>v^^<v<vvvv^<<>^^^vvv^^v><<v>^v<>>v<<<^>^>^^^>>^v<>v^<<v^<>vv^<<>v<^<>>vv>v<^v<^<vv>^>v<v>v<^><v<<<^<^^><<v<<>^vv<vvvv>v<><v>^<^v>^^vv>vvvvv^vv^<<><vvvv>><<^v<<<^>><v>>>>^^v<^v>>^^^^<vv^^>>>^<v<<>^<v<<>^>^><<^<^<v>>^<<<vv<>vv<>^<>^vv<^<v^vv^^>v<^^>v<v<^<vv<><^v^^vv^><^<><^>vvv^>>><<v^>v>^><>^<^>v><>v<<^^>>><<<v^>>><>^vv^v>^>^^vv<v<<v>><<v^<>^^>^<>v^^<^vv^<<^^>>vv^vv<^<v<<<>>^v<<v^vv<>v<^^^>v<^<<<<^v^>>^>v<<^<^v<v<>>>v<vv>vvv^v<^^^^><<>>>><^<<^^<^<v^<vv>v<>vv><v>>>^>v><>>v><<v<>v><^><<vv>v>v^<>^>^>^<<^>^<>^^<^>^^>>^^v<^<v>>vvv<<^<>^<v<^><vv>^><<v^<v>>v^^^<<<^>v>^^^<<^<<v^<>^>>><<<v<v>^>v<^v^>^>v^vv<^>><<vv>^vv<>v^^<v^>^<vv^^>v^>>v^<v^<><>v<>v^v>vv^vv>^>><>>vv>>><v^>^>v^^v^<^<>^^^^<^><>>^>>^><vvv><<<v^^v>^v><>>>><^^^>^<>v<>>vvv>v^>^v^>>^v>v><v<^<^<^<v>v^<>^^v^<v>>vv>>><^<v><<>>v>>v^v<v>v<<v>v^><v<<<>^^^v<<><<><<>^^>v<<^
>>><>><^^><>>^^<>^>v<vv<v^<<><^^vv><v>v<^v^><>^v<v>v>><<v^v<^vv<^>><<^>^<<><><<>>v>^^^><<<>^<<>vv^>^^vv>>v^><<<v<>v<<vv<<^^vvv^<>^^^v<^<^>>>^vv<^^>><^^>><v<^>v><^^>^>v^<v<^v>><v<^^>>>>><<^v^^>>^v<^^>^^v^^v^^>v<v^><^<^<>^v^v>vv^^v^<<>v^^>^<v>^>vvvv<>>^^<vv<v<>v^vv^>^v><^^>v^<^<>>>^v>>>^<^<v^^v<^v^><vvvvvv<^^vv>^><^vv>^vv<vv<v>v^><v><<<<<>^^^<v<^v<v<vv>^v^v>>^vv<<>^^v^<^><<^vv^^^^<><<v<vvv^v^v^>v^>>v^<^^v<>v<>v^>><v>v>^>v^v>>v^<vv^vv<>>>><<<<>^<^<>^<<^<v<>><v>v^<^<vv<vv>v>^>vv^<vvv>>><v<v>v<>^>v>vv<v>v^>v><v>^<v<^v^<>><^v><^>><^<<<<v^>>>^v>v^vv^^>>^v^>^<^vv>>>^><^v>^>v><^>v>v>^^<<<<^<<<^v<<<v<v<>^<^<><v>>v>>^<><>>vv>^>v^>><^><vvv<>v>>><>vvv<^>v<vv^>^>^^>v<<><<>v^<^^vv<<>v><^>>v^<<>v>^<^<<><^v<v<<>>v^^<^<vv><<^<v><>>v<^^>^<vv^<^^^><vv^^vv>^vv^v>>v<<>v^^^><<<v<<vvv^v<v>><^^<vv^v<>^vv>v^v<^>>>v>^<<<^<^v>v^>^vv<^v>>v<vvv<v<>^^v>>v<^^^^^vv^<v><><<>^v>><^<v^v>^v<^^>^^vv^<>>^><>v>vv<vv^^<>>v<^>v<<^><^>vv^<<<<><>vv><<>v^<>v<<^^^v<v<<<v<v<^<v<>>^<vv^><<<v^><<v<v<vvvvv^v><v<<<><<vv^>><>>^><^>v^v><
<^<v^^v^<^v^<^^^>v^^>v^^^^<v><v^><>^^><^^>v<^^^^^>>v>><v>>^vv>>v>>^v>v>>^^^<v^<>^^^vvv>v^v<vv>vvv^^^^<<v^^>>v><<vv><^v<^v>>^>><<v^^v>>v>^v<><^v<vv>>v>>>>>><>^<<<v^<><v^vv<<>>^^v<v^^^v><>>v>>^>>><^^>>v<<^^vv<v<^v^<<^v^<^^v>>v><^<>>>^v<<vv>^v<>>^^<v>^<^<<<>>vvv^>v^<^v>><>>v>^><>>>^^^^^<<<>^^^<^vv>>^>><vvvvv^vvv>^^^>^>^v<<^^vvv<>v^>v^v>><>^^vv>^>v<<^vv>^>v><^>>>^^>vv^^^^^vv^>v<>><vv>v>><<>>v^^<>vv><vv^>><><<^^<>^^><>^<^vv>^>v<^v<^>^v<v>^>>>>^<<>v^^>>>v^><>v^v>v>v>>v>>^<>v^><^vv^v>>>>^<^^v>^v^<^<^<^<>v>>v^^<<<^^v><v>^^>>^<vv>^<>^><v><<>><<v<v<<>>>^v><v^^>^>^^^>^^<>^v^v^<<^<v>^<v>><^>>v<>v<v<v^<>^v^^vvv>v>vv^>>^v<>^>v^^^>^vv<^v>^^>^>^v<<^<<<^v^<>v>>>><<v<^<>v^>v^vv^>^v^vv<>>^^^<^><>^^<^^>v>>v<<<><^v>^v^v><^>v>>^^^v^^><v<v><v^v^<<^<><v>><<vv><^>vv><vv^^<<^v<<<v><v^<>^v^<vv<>>^v^>>v^v^v<^<^>^v>^>v^v>vv^>^vv>^<^<vv<<^<^vvv<<><v^<>^>vv<<><>>v<<^^>v><v^>v>>^>^>^>vvv^<<v^v<v<>vv<<<^>^vv><^<>>v>>^<><><>^><<^>v^^<^vv^^><><>v><<<<v<><>^>>>>>>v<v^v^^<>v^^<>>v^v^><v><<<<^^^^<vv>>><^^vv>>^><^<>>vv<^><>
<<v^<vv<<<<^v<^<^v<v>vv^>^<<^^<<^><>v^vv<^^><^v^<^vv><<>^>><^^^<><v>v^><<^^><>^^^v<<vvv^<>^<^v>>^^^v^vv>>>^>^^v^v<v<^^>>^><^^><^v<^>><<><v>^<<>>v^>>^<vv>v^<^<>v^><v<vv>>vvv<^v>v<v^v^v<><<<^^<<>>><<vv<v^>^v<vvv<<^<>v<><^><<>><><<>^v^v<<^^vv^<v>><<v>^^<v>><^>>^>^<v><^vv>>v>vvv^<<v^vv<^<>>v>><>>^<^v<^^^>^v><>><<^<>^><<>^vvv>>v^^vv<vv<^<vv><><>^<^v^<^<^^^<^^>^^^v>^>^><<v^v^^<<^<>^v^>v<^<>>^^^<<^>^^>>^<>v>>v^><vv<<v^<vv<>>^^^>>^^^^>^<v>><v<v^v<^v^^<>^v>v>v<vv^<<^v<^v<^<v<<^^^<<v^v<<^v>>^>><vv<v<vv^^^v<<>>><<v^^v^<>^v><^<^^v^v^<v>><^^>>^^^>^<^<^<v<<^>^<^^^<v<v^<>>^^>^<^<vv><<v<><<^>^<<>>^v>vv^^><vv^<^v<v^v^><><^v<>>>v<^^vv<<^>^>v<^^v<^^<>^^v>>^<<>>vvv><<v^<<<v^><v<><v<v>v^<v<<<vvv^vv<^^<>vv<^^v>v<v^<<<^>><<>>v<<^<v<><<v^^v<v<^^^>>^<^>vvv<<<>v^<^^^^v>>><v>><^<^>^>^>vv<^v^v><^><v^>v>>>^v^>v<v>v^v>^>vv<^vv<^>>v<>><v^>vv>v>v<<^^^v^<>v<>>v><<<>><<<v^v^v^<<^>^<>>^>^<>>v^>><<v<^<<^^v^^^v>^<v^v<vvvv^^v><<vv>^>^<^<^>vv<>vv^<v^><><^<^^<>>^^v^vv<v<vvv<>^<^<>v><<>^v>v><><^<>><^v>v^>v^<^^v<^>v<>^^>v<v<<>
<><>vv>v>^v^^<>><^v^v^>^><<^<^<><<<^^>v^<<><>^^^v>^v>^<v^>^<>><<>^^<>^v>^>>^^^<^<v>v>^>>>v^<<<>^>v>vv>^<<<<^<vv<<>^v>^>^^^>><^<vv^<v^<v>v^<>v>>><<v^^<^v<>^<<<><^^^^^vvv>^vvv><v^^><^v><v><v^><v<v<^vvvv<><>v^^<><>>v<<<v<<v><^v>^>><<vv^^^v<<v>v<<<^vv>v<v^<>^^vv^v>^>^^<>vv>v^v>^^>^^vv^>><^>><^>vv<^^vv<v^vvv<^^v^^<^>v^v<v^<<v^v><vv^>v^<<^v<<<>^^<>v^^<>>>^><<^>v<>><v>>^<^^v>v^<v>^>><><^^vv<><^>v>v<>>^vv>vv^>v^^v<><^v<v^v><<<>>v<^><^>^v<><^>>v<^^><^^^^>>^<^>><v^v^v^>^^^^<<>^>^<>v><v^>>^>v^>v<>^>^^v^v^v<<<v<<<<^v><^v<<<^^<^^<^^>>>v>vvv>^v<vv>^>>>>^<<v^><^v<>v<vv>^><>^v^vv>>v^v>^^v<vv^>v<v^<>^^<>^<<vv><vvv<>>v<^><>><v<^v^<v^<<>^<<<>v<v>v>>vv^^^><<^^<>^><>^>^>><^<^<<<^<^<>v<>v>v>>^><<>><v>>>^v^^<<>v<^^<<^^^^<<>>v<>^^^<v^>^><v><v<^^<<^><>>^<^<^><<^><<^^>>^^>>^vvv>>v<<><>v^<>^^>>^^<<<>^^><>vv<^>>>>v^>>v^><^v><>v>^<>><v><><>vv><vv<^^<>>><>^>vv^^<><v<v<v><>^vv<^v>v^><^v>^^>vv^>v<^<>><^^v>><<^v<^<<>^v>v^v^v<v^<v><^v>v<v<v><<>>><><<^^v^><^<<v^^^^<<v>v^^<v><^^vv<^>^v^<>vv^^<>vv^^v^>^><<^>>>v<v>><<<<>><
<^v<><<v>^vvvvv>^<<v>v<<^v^>>^>><>vvv^^v^vvv^v<vv><>vv>>v^<<v>v^>^v^>v<>>^<<^>v^><><^^<>>^>v>v<^^<^<><vv<v<<^vv^<^>v>v<<<^v<<>>vv>vv><v<<v^v^>^<<>^^<<<v><>>>>^<<^v><^^^^vv<^v<vvvvv^>^<v><><^^>^>^^v>v<^v<<><vv^><>v<<>v^^v<<^v^vv>>vv><^v><>>>v<v<<^>^>v^<v>><<><vv>^^^>>>><^>v>^v>>v^<v^^<>^^^^^<<v>^^>><>^><<v<<v^<^<<vv>^^^>^v>>><<^v<^v>vvv^v^>>>>><<^>>^^vv^^>^vv^^v<<v><<v^<^^^v^>^^<>v^<><<vv<vv<v>v<><^^<^v^v<^>>^^>>vvv<^^<v>>vv^^^^v<>^vv^>^<vv><^<v^<>>><vv>>>^>vvv>>^><^vv^v^^^<v^><^><^<^^<^>v<<>^<^v>><>>>^vv<<><>^vv^v><^>^<^>>>><>v^^^>v>^v>^>><><<<^<v^vv>>>v><v<v>^v><<><v^^>^<>v<^<v>><v^^>>>^<<vvv>^v^v^^^<v><>v>v^>v^>><^^<<v><^><<<>vv<^>vvv<v<v^>^><vv<^<<>>v<^<^^<^>^v<<^<v^<vv<<v>>vvv^v^<<<^>^<^<><v^>>^^v>^<^^^v^>><<^v^v>><><>>^<>v^v<<v<^vv^<>^vv<^v<^vv<<<>^<><^v><v>^>v<<^>v^<<vv>^vv><^^<^<<^v><<><>v>^<>>v>^vv>v^<>vvv<>><<v^v^<v^^<v>^^><><v>><v<>><vv<>>^<v^>^<<vv>^>v><v<^v<v><^<^>^^>>^<<v>^v><>^<^^>vv^^^>vv^><v<<^^v^><vv^^^<<^v<v<>>^<^<^v>^>>vv^v>>v<v^v^<vv>^v<vv>vv<>v><^<<<>^v^v<<<<<<v>^>
v>>v<v^^<<^v<<v<>^<v>>^>v^v^v>^vv<v^^vv>^^<<^<^^^^^vv<>v<v^>><^^>>v<<>>^>v>v^><v>v<><^v<<vv>v^vvv<>>vv<^<>^^^^<>^>v<>^v<<<v<^v>v^>v<>^<<>v^<vv<^<><v>^>^>vv>^>v>><><v<^v>^v<<><<<v<>>^<<<<vvv<vv^<<^vv<vv<^<^v<<^vv<^v^v<<v<<<><>^^v<^^>>^^<<>^vv><<^v>v>^v^<v>><<v>>>>v^>^<<^v<><vv^<^v<v^^<v<vvv^vv^^v>^<^v>v<<vv^v>^v<v^v<^^vv<>v>>v><v^^<vvv<^<v>^>v<<>vv<v>^<<><^v>><^>>>^v<<v^>^^<v>^>vvvv<^<<<^<v<<^>^^^^<^>^>v^<^vv><v<>v>>v>v^^<v>vv<vvv<^^><<<^<v>vv^>^<v<><^v<<<^^<^>^<>^v>>v<>>vv^v>>^<>v^<>vv><<>v>^<<>^<vvv^>v>^<<><^<v^v>v>v<<vv<^><vv^<>^>^^^>>>>^v>^^^vvv^><^^^<><v>>^v<v>v^>v^>v^vv^^>>>^vv>^^<>^><v<^><<^<v<><^><<<^^^>v>^vv^v^^^v><>v<^vvv>^>v>^^^^v^<^v><>v>^^<>^^vv><<>vv><<v<<v^>v^>>v>^<^<v>>^vv<>^^^v^vvv^^v^^<vvvvv>v^>vv^vv>vvvv<^>>^<>><<>v>^^vv^v^>v>><^^v>>^>^v<>^>v><<<v>>v^v><<>vv><><^^^<vv<<<^^>>^v>^<^>><vv><>>>v^v><v<^<><v><><<<v<v>v^v>vv<<<>^v<vv>v>^vv<^><v^<>v<v<^>v><>vvv>^v<^>>v^><<^><^><^>>>vvv><<v>^>>^^vvvvv<>^^vv>>v^v^v^v>^>>^v<<v^>v^v>v><v<<<v^>v><^^vv><<v<><>^^^^^^v^>^<<<>v<^v>^vv
v<v>^><^<v>^<^><v<vv^v<^vvv^<v>>^v<<><^v>^^v^<><<<>^<v<v>v>>>^>v><>v>v^^v<^v><^<^>v<<><><>^>^v>>>><>vv>>v>^^<>v^<<v<^v<<vvv<<v^v<vv^<<v^>^^>>^>^^v<v>v<^<>>v>v<v<^vv^<>>v^<><<^^<^<><^<^vv^^v<^v<^<v<^>><<^>v>^>^>^vv><v>v>^>vv<<>vvv<>v><<>v><^^v<>vv>v<<v<^<vv>vvv<<^^^^v^>^^^<v>^^<<<<vv^<<v><>^^^^>^^^<^v<v><^<^v<v<>^<^<^^^^<<<^^<vv^^^<<v<^v>^>>>v<<<v^>>vv^^<v<>vv^>v<v<v^>><v^><vv<<v^^<^>^v>^<>v^<^v>v^>>v<<^<>><>>v^>>v^^>v^vvvv^^v<<<<v<v>^>>>vvvv<<v><>v>^>^<v^<>><vv^>>>v^>^v>^v^^v^>>^^v>>>>>>v><^<^<>v>^>>><>><^><<<v^v><^<^v><vv^<>^v^^>v>>^^<<v<>>><^<<^v>^<^>v>^<<vv>^<<v^>^v^><^<>>>>><>>^v<><<^v>vv<v>>^v<^>vv<<><^>v^>>vv^^^<^<^vvv^<<>v^>^v<>>^vv<^^<^>^<^<^vv^v<<^v^v<>>^<v>^^<v^>v><>>vv<>^^>^^<<><^vv^^<<v>v>^v<>v^><<>v><>v>>v><><v<>>>vv^^<v^^<>>^>^^^>>v<<v<^><vv>>^<>>>^<v>^>^v<v>>>v^vv<<<vv^<<<v>vvvv^<<^<<vv^<^<^^v^vv><v^^v<<v^v<v^<<vvv><v^><<<vv<>><vv>v^><^<v^vv^<<v^v^^>>>>v<vv^><^><><v^<v<v<^<v<>v^v^v<^<^<>><v^^<v^<<>^<><<<v>>>^<>v><>^^<>vv<^^^v<<^>^>v^>^^<>^vvv><<>>^>^^^v<<^<vvv<<>><v^<<>>
v>^v>^>v<^^^vv^v>^>>>^v>v>^<vv^^><^>^v>^^vv>>^vvv^<^vv><v^<<><><>vv><>^>>>^<<<^>>>^v>v^<v<<<v<>><^^><v<<^^vv^v^<^^v>vvv>><>>v^<^<<>v<v<^<<vv^v><^>>><^vvv<^<^>^^v<v>>>>^><>>^>^>v>v>>><v>v>><><^^>^^^v>^<>>vv>>><vv^vv^v^^<^v>v<>^><>><><><>>^>>v><><^vv>>>^<<^<^^v>^<<<v^>v^><v>>v>vv<^<v^>><^>^>^<^vv<>^>v<^<^><^>^^>>^^^vvv^<^v<<>v>^v><>v><v<v<v>vv>v>v<>><^v<<<<^>v>^>vv^<<^v^>^>><<<v<>^>v>vv^<v<<>^<<^v<>>v>v^><<>vv^>^<v<>^vv^^<<v>v<<>v><v<v<<^v^^^^<>v^<^>v>v<v<<><^<v^^>^v>^^><^><>>>v^<v^v^<v^v<><^<^<>>v>^^v>^><<<v>^^vv>^>><<><<<><^><>^vv<<><^v<v<^^>><<<v^^>vv^<><vvv<^<^<^<^^^<<v>vv^v^^v<<v<<^v>^>^^^^<v^<v>^><vv^v^v>><>vvv^>v^>>v><^^v^>>v>v>v<vv^^v<vv^^^<>^v><v><vv>v>v>v>v<>^>>^>>v<>^>^v<^<><<^<^^^>^^>^^>>v<<v>vv>v<>><vv<^<>>^>><v>^v<<>>><>><<>v^v<^>vv^<<^<<>><>^<>vv<vv<>>>v>v><^<v<^><><vvv<><v^v>>^>>>^vvvvv>^<<<<^>v^><>v<>><^>^<^^^vvvvv>><vv<><>>v<<<><v>>v<<v<>v<^<>^<v>v^v<^v<<<>^v>>^v^><v^<><<>>><>^^<<<<^v^^<^>>^<<<^v>v^>v<^v^<>^<>v<v^<<<><^v<vv^v>^v>^^<>v<>^<^>v>^>v^<<^vv^><>^v^^<><^v><<<^<
<^v>vv>vv^>vv<v^<v>>v>>vvv^>^><<^^^v>><v^^>^>^v>^<^^><v>v<<><<<>v><v^^>^<^><^>^<^^<<v^<<vv>^^<^>^>vv>^vvv^^><^^v^v>><^<>>v>^<^>^<<v>v^vvv<<v>^^<>v>v<v<v^^<<^^^^^<v<><<^v>v><<>>^v^v^>>>vv<>v^>v<vv<>vvv<vv<>^^^^^v<^v<>v<><>v>>^v<<<^<>^<<><^v^<>v<v><>^<<v^v<><^>>^><vvv>>>>>vv>^v><v><><^v<<vv>v>>>^v^><^>^v>>vv<>^v>v^vv<>>^v>^^^v>^v><^v>v<^>v<>>^vv>>>vv^>^<>^<v^v<<>v^^>>>>>^^v>>>vv>>>^<<>v<>>>><^v>><>^v>>v^^v^^v><^>^v^v^vvv<<>^v>v<>>^><v><>^v^><v<><<>v<^v><><^^>>v>v^v<v<>v^<>>vv>>^^^v>v>><^v><<^v<^<>vv<>><v>vvvvvv>^><v><^^>v<v^<<v<<<>^<v^v<<<<>>><>^^^^<>v^v<>vvvv>^>>^<v<<>v<>^^<v<v><^>v^>^^v<>v<^>>vv>v^v<v><<v>vvv<<v^><<>vvv^<<v<>^<<><>vvv>>^<<^<><<<v^<>>>vv>v^<>v>^^>v>>v>^v>vv<>>>v>v^^^>vv<v>^v<<^>>>v^^^>^^v>><>><>^<^v^<>^><>^^^v>^v><<>^v<<v>^v^<^<>^<>^<<^<vv<<>^^vvv>vv><<>^><v^>^>><><<v<^>>>v><v^v^<>^<>^vv>v><v^>>^<<^^v>>^<^^>vv<^<^<v<>^>v^v><vvvv^v>><v><vv^v<<^>vv>^^>^<^^^<>v<v>v<<^><<^>^^>^v^^^>>v^vvv<>>v<^>v<v^>^>^<<^>>>>><<<^<<<^<<^><>>>^<>v>>>><v^v<vv>>^><<>^>^<>v^<^^<>v<>v>^<^^^<^>>
><>^<^^<>^>v^v>>v^<<^^vv>>^v^^>vv<^>^^^v>^><v<>^<<>^v^v<<v>^^^><<v^>^<^^^<vv>^>^<vv<v^<^^^>v^v>^>v>^<<>>^<v^<>vv^>><^>>>v^<>v^<>>><>>vvv<>^><v^v<<^v^^<>v<><<^>>v<<<v^>^v<>v^>><^^^^>>v^v^v>v>^v^>v^vv<<^>v^<^^v<<vv<>><^^v><<vv^v^><vv><^<^<v^v<^<>^>vv^><^^^^><^v<>>vvv<>>>v>^^<><<<^>v<v^<v>^vv>vv>v>^v>^<>v^<^vv>>^<^>><v<<<v<>^^^><<^<v^>v>v<>>^^>v>v<^>^^>>vv^v<<^<>^>><^>^>^><>^<>^^vv><^<><>><v<^^<><^v^^>vv^v^<<>>v>>^vvvv^>v><^>v^^v^<>><<>^^>^>^>v<>>v>>^v>v><^<>v<vvv>v>v^v<^^>v<<<>>^>>^<>><v>vv^>v>>v^><<<<^^>^v>^^>>^>><<^v^>^v^v>>^^^>^>><>v<<^>^^<^v<>v^v<>>v>vv>^v>>><>^<<<v><v<<v<<^<>>>><>v<v^^<vv^<><^v>v^><v<>><^>><^><<^v><v>>v>>>^<^vv^v^>v>v<^<^>>v<v><<v^^>^vv<vv^<<^^^>^v<v<<<v<v^>><v<<>><^>v>^>v>vvv^<^v^^<^^v^<v^v<v<><^<<<^vvv^><^><^<<><^>^>><><<vvv<<^>v>v^<v>>^<^^>v<<<<<>>><><v>><<^v^vv^>>>^^>^^^^^>>v^<vvv^>><<>v<^v^v<^v>>v>^v><<v<>^v^^v^<vv<><vv>>v^<v<<<^>>^v^>vv>v^>>v>^<><^>vv^v>vv^<<v>>>^v<>><^><^^<>>><<<^vv<^^v<^>><<<>><v>>^<^><<<v<v<v^^<><v>^vvv>^<>v>v^v>>>^^^<^>^>>v><<<><^<v<^>^>^^
<v^v<v>>><>>^>><v^<>>^^>>^^>>><^^v<^<^>vvv><v>vv^<>v^^<><v^<<>v<>vv<>^<v<v<^><^v^>^^^>^>>v>^>^^<>v<<<^^><<<<><^v^<v<vv^v^^<^<^^>><><vv>>^^<v<^<><^^v<>v^vv<v^v^<>v>><>^^^>><<^v<^>v<^^><^<^v>><^<^v>>^>>v>^^^^<v^<<^<>^<>^v<vv<>>>vv<v<>^><>^^<vv<><^<^v^>^>><^vvv^^>v^^v<<^>^^^<^><v>v<>^^v>v^v><><v<<^>v^<<^vv>v^^v^<vv^^^>^^^<v>>^<^<<vv<v>>^<>^^v>^<^^>^>>><v^vv>>v<<><><<^vv^v<^<^^>>^><^v^<<^<v<v<v<<<<<<<>v>v<v><>^>vvv^^vv^^v>^>v<<vv>>v<vvv>vv<>v><^v><>>^><^^^>>^<vv>^>^^v^>^<^^v<>^^<>>v^^<<v<<^<^<^vvv<<^v>^^vvv<<<><v>^v^^<<<^>>v>^<<<^>vv<v><<>v^<><><^>^<>><><^^^^v^^vv>vv<<^^v<^^^<vv^^^vv><<<<v>><<>>^<v<v^^v<<>^^v<><vv<vv<v^>vv<>v^><><><<>^>^<<<<<vv<<^vv<^<><<<>v<v<<^v>>^vv<<^>vv^v<v<<vv^vv>^v^vvvvvvvv<v<vv^>^<>^^vv>^^<^>vv>^^<^<vv^>^>>>vv^^^^><><^<v<^>>>>><<^^v<>^v<^^>v<^^^>^^^<v<^<^v^<^>vv<>^<^v>><<<<>v><^>^><v<<^^^^<<v^<>>vv>v<^^^><^v^>^<>vvv<^v><><v<v<^v<<<<v>v^>v<><>v<<<<<v<<>>v^v^vv<>v<vv^v^vv<<>^^>^<<^<>>vv<>>v<v>v<v>v<^>^<v<^v>^^v<>^v^^vv<^v^v^v^><><^^<^^>v>><<v^>>^><>>>v^<v<>^^>><<<<>>
^v<>v^<>vvv<^^<>>^vv^v>v<^<v^>^^>^>vv^^^<><<<><^v^>v<<><v>^<><>>>vv<vvv^v>><^>>vv>v^<v>v<>^<^>v<<^^><<<>>><>>v<v><<>^^<<v<>vv^^>>vv>^^v^^^<^^<v^^<>vvv^v<>>^v<>>^v^><^v^^<><v>><<^vvv<^>v<<^>v<^v^v>^^^^><vvvv>>^^>v<>^^>^v<>^v<^<^^<<<^<vvv<^<^vv^>^>>>^^><>vv<^>>v^v<>>><^>><^^>^v^><<<vv^>><>>^>^<^><v>>><><>^^v^<v<^<>^>>^<^>^<^^^v<^<^v>><v<v^<^<v^<>^^>v><^>v<><<>^^v^><<<<v<vvvv<>>><<<>>^v^<^^>>vvv><>v>^v>vvv^^>>><>>>>v>^><>><^>>^v<v<<><<<^<^^^>v^>^<<>^v<>^v>>v<^<v<>^<v<v<^^^^^<><^<^^<^<v>>vv^<>><v>v^v>>><^v<>v><>^v>v^^<<^v^^<^<v<^<^vv<>v<^^<^vv^<><<<^v<^<^>v>>>^<^>^<v^>v^^^<><>^^v><^^^v^v^>v><><^v^^<^<v<^v<^^<>v^^<^>vvvv<<^<<v^<^>>v<v><^<^>^^>^vv<v<>v^v<^>><vv>^<<^v>v>>v><><^<>^<v<v<^>^<<v><v^vv^vvv<<<v^>><^v<<>^><<><^^><^<^v<v<>v<<<<>^^<^<vvv>>^><<^>>^v<^<^^<^<><^<v^^><^v^^>^v<^^<<>^^>v^<^v<v>v<>^^<>>>v^v<<^><<vv^<<^^<v<v<>><v^>^<vv^><^>>>>>^<<><>^^^<^>v>v>>>^vv<>v>^<>^><>>><<^>>vv>^^>^v>>>>vv<<<<^vv>>^<^>^<v^vv>>^v^<^v<vvv<><^<v>^^v<<^>v>v>^v^>^^<<vvv><<v^><<v^v^>>v>v^<>^^^v<^vv>>v>>>vvv<
<>>v^^<<<v^<<><v^^v^^>><^<><<>><><>^<^<^<<>>v><^><^<<v<>vv<^><<v^>>^><>v<^v^><<vv<^<v<^<>v>v^<<v>^>^vv>^^v^<<^v<><v^^<^^^>>>>v^^vv<<v>v^^v^>v>vv>v>^v>v<v><<^>>^><>^>^>>^vvv^^<^^>^<>v>>>^<^<^^>v<v<<>v>>v<^<^><><v>v>v>vv><v<^>^^<^<>^^>v<^><vv>^v><v^>vv>vv>^<><^vv>>^>v>^^^<vv<>v^>>>^<<^><>>v<v<vvv^vv<^^>^<<^>^<^>>^vvv<><v^^>vv<v^<^><><^<v>>>^><^<^vv<><vv<>v<<<v<^<^^^<<>>>>^<<v<vvvv^<>>vv^v>^><^<<<>^v^><^<^v<^v^<>^<^^v^<v<>>v>v>v>v<<<v^^>>>^v^<vv^vv<^>v>v<<vv^^<>^^v^<^><^<>v^<>v<^>v^v>^^<<><^>>vv>^v>v<><<^^v<^v>vv<>v>^v^v><<^<v<>>v><v>v^v>^>v^>>>v><><<v><>^v<^^>vv<v^<^v>v<vvvv^<v<>v<^>^>v<^<>>><<^>>v>vv^>v<v^<<<^vv>>^v<vv><<^<vv^><vvv<<>>^>>v>vvv<^<<v<>v<<v<v>vv^<>^>><^^>^>^v>^<>>>v<vvvvvv<vv>^<v<^><>>>v<<><v^v><^^^v^^<<>^v<>^vvv<^<<v<>^v<v^^<vvv<<<><^><^<^^<^^<^<v^^^>^<<>>v^v<^>>vv>vvv<>^<v<<<^><>v<<vv<><^^v<<^><<<v>><<>^v<^^>^<^^<v^<v><><>>>v^^^v^^<>vv<<>v<vvv>>v<<vv^v^v^>^vv^^^>^>vv^<^><<>^>><>^<<vv><><<><^<^^v>v^v^^^^><v>^^v^<<<<v^v<v^>v<vv^vv><<<vv<v<>v<><^^<<v>v^^^<>>>v><^^v><v^>>^v^
<><vvv>^v<<<>^<v<<vvv<v^><>^v^^>^^><<^<<v>vvvv>>>^>^^<><^<>^><v><v<v><><<v^<><><>^<v>^^^^>^><<v<<vv>>^>>^><^>^>^>v<v>^vvv<v>^>v<^>><^^<<>>v>>v^v>>^><<^>v<>^v^<^vv<^v>^^^v^v>v>vv<<v^v>><>v>>^^v^vv<>>^vv^v><><vv<v^<>^>^^>vv^v<>vv<<><<<^v^^vv^>^<>>^<<<>><^^<<^<><>v^<v<v^>>^v^v><<v>v^>^<><<^>>>vvv^vv>vvv<v>>v>v<^<<>>v<>^>>^><<<<v^><<^>v^^v<>^^^^<<>^^vvv<^<v<>vv<>v<>>>v^>^>>^<<^^^<v<>^>^<<><v<>>^^^><vv^^<>vvv<>>^<>^^^<v>v^^^>vv^v><<<><>^^>^<>v<^^><>^>>>vv^><<vv^>vv<<>^^<<v>^>>^^><>>^^^^><^<>>v<<^^^v<><v>v^^^^^><<><v>v>^<<^^v>vv><v<v<^>>>><vv^v<<vvv>v>vv^^^^<<<^v^>^^^^vv>v<>><v>v^<^v^<^>v>vv^<<<<>^vv>v>^^vvv>v^><>^^<<>><><><><v^<^<vv>>><<vvv<<v^>^^><v>v<v^v^^^^^v<^<^^<>>vv<v<vvv<vv^v<<><^v^><v^vvv><v<^<v^^v<vv<vvv^^^^<><><>>^v^^^>>vv<>^><>^><^<>v<<v>>v><<^><<vv^^<<^>>v^<^^>>^v>v<^<<v<>v^v^<^v<>^v^v<>v<vvv^^v><<><<v<>>^v^v^<>v^><<>^>vvv^<<>v<>^><^<v^v>>>>>^v^^><^^><v<<^><^v<^^<^<>><>vvvvv^vv>v>^<<^^><>><^^><v^^^<>>^<>v<^v><vv<v>^>v^v^^<v^^<<^<v>>>>^<<^<>^>^<<vv<v^v>vv^^vv>v>>^>^^>^>>>^>vv>^v<
v<v^<^^^<<v>^^vv^>^^<^^v^>>v><>^>vv><v^v>v>^v<<^<^>vv>vv>>^>^v>^<^^vvv><vv>>v<>^<v^v<^<v>^>>>>v^v^^vv^<<v><><^vv>v<>v>v>^v>^<vv>>^^^>v<<<<v^v>^vv>^>v^>v^v>^<v<vvv><>><^>>v^<>^^v><>>v^<^v^v>>>^v>><<<^<vv<^<<<<>vv<^><<v>^<>><v^v^<^<^<><<<<<<<v>><^^<^<<<<<>><^v>>>^^><^<^>^vv<^vv<^<>><v^>v>^<v^<v<vv<><^>><>v>^<^^><^<>v>>v^<>>><v><>^<^<<^vv^>>vv^>v^><v^><^v<<<vv<<>><^>v<^>v<>v><>^<><^^>^<<<^^>>>>v^<v^v^><<^>>vvv<v<>^>><<>>>^<^>v>^>>^>v^>v^>^^>><>v^>v^<>^>^>>^^v>>v<<v<>vv>v<<^<^<<v^v>^<^v><><^<^^^>^v^>^<<v<>>vvv><<v>^^^>>v><v^v<<<^^>v>v^^<^^^>^^<>><<v>vv><><^>>^<<v><v<>><<^v<vvvv>^<v^^v><>v<><^><>>^^<<vv<^>^^>><<><>>v><<>>vv^><v>v^vv>^>^^<<^^<>vv><><<v^^<>v^^v>^^<^<v^>^v<>^v^^<<^^v>v^>vvv^v<vv^vv>v^><><v^<v>>^<<>v<<v><v<<>>^>v>><v<>v><<<<>>v>>^^<<><v^<<<<<>vv>v^v>v<v>^^<>vvv>^<<^>^>^>^>>><>>^>v<>>^<v<>>>v^<v>v><v>>vv<<v><>v>>v^v>>vvvvvv^^>><>^v^vvvv>>>v^<^>^<>vv<vvvv<^^v<^<>^<v^<<^<v<^^v^^<v^<^<^><<<^<<^<^^^^<<v>>v<^>v^<>vv>><>^<<v^<^^^>><vv^v^>^v>v>^^<^vvvv<v^vv<v^>vv^^>>>><^<^^<<<vv>>>v^<v"""

text3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""


def parse_input(text):
    warehouse = []
    robot_pos = None

    grid = text.split("\n\n")[0].split("\n")
    moves = text.split("\n\n")[1]
    
    for y, line in enumerate(grid):
        row = []
        for x, char in enumerate(line):
            if char == '@':
                robot_pos = [y, x]
                row.append('@')
            elif char == 'O':
                row.append('O')
            elif char == '#':
                row.append('#')
            else:
                row.append(".")
        warehouse.append(row)

    move_sequence = moves.replace('\n', '')
    # print(warehouse, robot_pos, move_sequence)
    return warehouse, robot_pos, move_sequence

def move_position(pos, direction):
    y, x = pos
    if direction == '^':
        return y - 1, x
    elif direction == 'v':
        return y + 1, x
    elif direction == '<':
        return y, x - 1
    elif direction == '>':
        return y, x + 1

def make_move(grid, start, end, direction):
    temp_r = start[0]
    temp_c = start[1]
    new_robot_pos = end

    while temp_r != end[0] or temp_c != end[1]:
        if direction == '^':
            grid[temp_r+1][temp_c], grid[temp_r][temp_c] = grid[temp_r][temp_c], grid[temp_r+1][temp_c]
            if grid[temp_r][temp_c] == "@":
                new_robot_pos = temp_r, temp_c
                break
            temp_r, temp_c = temp_r+1, temp_c
        elif direction == 'v':
            grid[temp_r-1][temp_c], grid[temp_r][temp_c] = grid[temp_r][temp_c], grid[temp_r-1][temp_c]
            if grid[temp_r][temp_c] == "@":
                new_robot_pos = temp_r, temp_c
                break
            temp_r, temp_c = temp_r-1, temp_c
        elif direction == '<':
            grid[temp_r][temp_c], grid[temp_r][temp_c+1] = grid[temp_r][temp_c+1], grid[temp_r][temp_c]
            if grid[temp_r][temp_c] == "@":
                new_robot_pos = temp_r, temp_c              
                break
            temp_r, temp_c = temp_r, temp_c + 1
        elif direction == '>':
            grid[temp_r][temp_c], grid[temp_r][temp_c-1] = grid[temp_r][temp_c-1], grid[temp_r][temp_c]
            if grid[temp_r][temp_c] == "@":
                new_robot_pos = temp_r, temp_c
                break
            temp_r, temp_c = temp_r, temp_c - 1
    
    return grid, new_robot_pos

def perform_moves(warehouse, robot_pos, move_sequence):
    for m in move_sequence:
        # print("Move: ", m)
        temp_pos_r = robot_pos[0]
        temp_pos_c = robot_pos[1]
        empty_space = None
        if m == '<':
            while temp_pos_c-1 > 0:
                if warehouse[temp_pos_r][temp_pos_c-1] == "#":
                    break                
                if warehouse[temp_pos_r][temp_pos_c-1] == ".":
                    empty_space = (temp_pos_r,temp_pos_c-1)
                    break
                else:
                    temp_pos_c = temp_pos_c - 1
            if empty_space != None:
                warehouse, robot_pos = make_move(warehouse, empty_space, robot_pos, m)

        elif m == '>':
            while temp_pos_c+1 < len(warehouse[0]):
                if warehouse[temp_pos_r][temp_pos_c+1] == "#":
                    break
                if warehouse[temp_pos_r][temp_pos_c+1] == ".":
                    empty_space = (temp_pos_r,temp_pos_c+1)
                    break
                else:
                    temp_pos_c = temp_pos_c + 1
            if empty_space != None:
                warehouse, robot_pos = make_move(warehouse, empty_space, robot_pos, m)

        elif m == '^':
            while temp_pos_r-1 > 0:
                if warehouse[temp_pos_r-1][temp_pos_c] == "#":
                    break
                if warehouse[temp_pos_r-1][temp_pos_c] == ".":
                    empty_space = (temp_pos_r-1,temp_pos_c)
                    break
                else:
                    temp_pos_r = temp_pos_r - 1
            if empty_space != None:
                warehouse, robot_pos = make_move(warehouse, empty_space, robot_pos, m)

        elif m == 'v':
            while temp_pos_r+1 < len(warehouse):
                if warehouse[temp_pos_r+1][temp_pos_c] == "#":
                    break
                if warehouse[temp_pos_r+1][temp_pos_c] == ".":
                    empty_space = (temp_pos_r+1,temp_pos_c)
                    break
                else:
                    temp_pos_r = temp_pos_r + 1
            if empty_space != None:
                warehouse, robot_pos = make_move(warehouse, empty_space, robot_pos, m)
        # print("warehouse:", warehouse)
    return warehouse

def find_gps(text):

    warehouse, robot_pos, move_sequence = parse_input(text)
    warehouse = perform_moves(warehouse, robot_pos, move_sequence)

    total = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "O":
                total += (i * 100) + j
    return total

gps = find_gps(text)
print("gps: ", gps)


def scale_grid(grid):
    scaled_warehouse = []
    for row in range(len(grid)):
        scaled_row = []
        for char in range(len(grid[row])):
            if grid[row][char] == "#":
                scaled_row.extend(["#", "#"])
            elif grid[row][char] == "O":
                scaled_row.extend(["[", "]"])
            elif grid[row][char] == ".":
                scaled_row.extend([".", "."])
            elif grid[row][char] == "@":
                scaled_row.extend(["@", "."])
        scaled_warehouse.append(scaled_row)
        # print(scaled_row)
    return scaled_warehouse


# Following approach, similar to part 1 would not work here: particularly for vertical movement
# def perform_scaled_moves(warehouse, robot_pos, move_sequence):

#     for m in move_sequence:
#         print("Move: ", m)
#         temp_pos_r, temp_pos_c = robot_pos
#         empty_space = None

#         if m == '<':
#             while temp_pos_c - 2 > 0:
#                 if warehouse[temp_pos_r][temp_pos_c - 2:temp_pos_c] == ["#","#"]:
#                     break
#                 if warehouse[temp_pos_r][temp_pos_c - 2:temp_pos_c] == [".","."]:
#                     empty_space = (temp_pos_r, temp_pos_c - 2)
#                     break
#                 temp_pos_c -= 2
#             if empty_space:
#                 warehouse, robot_pos = make_scaled_move(warehouse, empty_space, robot_pos, m)

#         elif m == '>':
#             while temp_pos_c + 2 < len(warehouse[0]):
#                 if warehouse[temp_pos_r][temp_pos_c + 2:temp_pos_c + 4] == ["#","#"]:
#                     break
#                 if warehouse[temp_pos_r][temp_pos_c + 2:temp_pos_c + 4] == [".","."]:
#                     empty_space = (temp_pos_r, temp_pos_c + 2)
#                     break
#                 temp_pos_c += 2
#             if empty_space:
#                 warehouse, robot_pos = make_scaled_move(warehouse, empty_space, robot_pos, m)

#         elif m == '^':
#             while temp_pos_r - 1 > 0:
#                 if warehouse[temp_pos_r - 1][temp_pos_c:temp_pos_c + 2] == ["#","#"]:
#                     break
#                 if warehouse[temp_pos_r - 1][temp_pos_c:temp_pos_c + 2] == [".","."]:
#                     empty_space = (temp_pos_r - 1, temp_pos_c)
#                     break
#                 temp_pos_r -= 1
#             if empty_space:
#                 warehouse, robot_pos = make_scaled_move(warehouse, empty_space, robot_pos, m)

#         elif m == 'v':
#             while temp_pos_r + 1 < len(warehouse):
#                 if warehouse[temp_pos_r + 1][temp_pos_c:temp_pos_c + 2] == ["#","#"]:
#                     break
#                 if warehouse[temp_pos_r + 1][temp_pos_c:temp_pos_c + 2] == [".","."]:
#                     empty_space = (temp_pos_r + 1, temp_pos_c)
#                     break
#                 temp_pos_r += 1
#             if empty_space:
#                 warehouse, robot_pos = make_scaled_move(warehouse, empty_space, robot_pos, m)

#         find_scaled_gps(warehouse)
#     return warehouse

# def make_scaled_move(grid, start, end, direction):
#     temp_r = start[0]
#     temp_c = start[1]
#     new_robot_pos = end

#     while temp_r != end[0] or temp_c != end[1]:
#         if direction == '^':

#             grid[temp_r+1][temp_c], grid[temp_r][temp_c] = grid[temp_r][temp_c], grid[temp_r+1][temp_c]

#             if grid[temp_r][temp_c] == "@":
#                 new_robot_pos = temp_r, temp_c
#                 break
#             temp_r, temp_c = temp_r+1, temp_c
#         elif direction == 'v':
#             grid[temp_r-1][temp_c], grid[temp_r][temp_c] = grid[temp_r][temp_c], grid[temp_r-1][temp_c]
#             if grid[temp_r][temp_c] == "@":
#                 new_robot_pos = temp_r, temp_c
#                 break
#             temp_r, temp_c = temp_r-1, temp_c
#         elif direction == '<':
#             grid[temp_r][temp_c], grid[temp_r][temp_c+1] = grid[temp_r][temp_c+1], grid[temp_r][temp_c]
#             if grid[temp_r][temp_c] == "@":
#                 new_robot_pos = temp_r, temp_c              
#                 break
#             temp_r, temp_c = temp_r, temp_c + 1
#         elif direction == '>':
#             grid[temp_r][temp_c], grid[temp_r][temp_c-1] = grid[temp_r][temp_c-1], grid[temp_r][temp_c]
#             if grid[temp_r][temp_c] == "@":
#                 new_robot_pos = temp_r, temp_c
#                 break
#             temp_r, temp_c = temp_r, temp_c - 1
    
#     return grid, new_robot_pos



def perform_scaled_movements(grid, moves):

    rows_len = len(grid)
    cols_len = len(grid[0])
    grid = [[grid[r][c] for c in range(cols_len)] for r in range(rows_len)]

    for r in range(rows_len):
        for c in range(cols_len):
            if grid[r][c] == '@':
                sr,sc = r,c
                grid[r][c] = '.'

    r,c = sr,sc
    for m in moves:
        dr,dc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[m]
        rr,cc = r+dr,c+dc
        if grid[rr][cc]=='#':
            continue
        elif grid[rr][cc]=='.':
            r,c = rr,cc
        elif grid[rr][cc] in ['[', ']', 'O']:
            Q = deque([(r,c)])
            SEEN = set()
            ok = True
            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                rrr,ccc = rr+dr, cc+dc
                if grid[rrr][ccc]=='#':
                    ok = False
                    break
                if grid[rrr][ccc] == 'O':
                    Q.append((rrr,ccc))
                if grid[rrr][ccc]=='[':
                    Q.append((rrr,ccc))
                    assert grid[rrr][ccc+1]==']'
                    Q.append((rrr,ccc+1))
                if grid[rrr][ccc]==']':
                    Q.append((rrr,ccc))
                    assert grid[rrr][ccc-1]=='['
                    Q.append((rrr,ccc-1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for rr,cc in sorted(SEEN):
                    rrr,ccc = rr+dr,cc+dc
                    if (rrr,ccc) not in SEEN:
                        assert grid[rrr][ccc] == '.'
                        grid[rrr][ccc] = grid[rr][cc]
                        grid[rr][cc] = '.'
                        SEEN.remove((rr,cc))
            r = r+dr
            c = c+dc

    updated_grid = []

    for r in range(rows_len):
       updated_grid.append(grid[r])
    
    return updated_grid

def find_scaled_gps(text):
    warehouse, robot_pos, move_sequence = parse_input(text)
    scaled_grid = scale_grid(warehouse)
    scaled_warehouse = perform_scaled_movements(scaled_grid, move_sequence)
    
    total = 0
    
    for i in range(len(scaled_warehouse)):
        for j in range(len(scaled_warehouse[i])):
            if scaled_warehouse[i][j] == "[":
                total += (i * 100) + j
    
    return total

sacled_gps = find_scaled_gps(text)
print("gps: ", sacled_gps)
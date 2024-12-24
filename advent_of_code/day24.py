from itertools import combinations


text1 = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

text = """x00: 1
x01: 1
x02: 1
x03: 1
x04: 0
x05: 1
x06: 0
x07: 1
x08: 0
x09: 1
x10: 1
x11: 1
x12: 1
x13: 0
x14: 1
x15: 1
x16: 1
x17: 1
x18: 0
x19: 1
x20: 0
x21: 1
x22: 0
x23: 1
x24: 1
x25: 0
x26: 1
x27: 1
x28: 0
x29: 0
x30: 0
x31: 0
x32: 0
x33: 1
x34: 0
x35: 0
x36: 1
x37: 1
x38: 0
x39: 1
x40: 1
x41: 0
x42: 1
x43: 0
x44: 1
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1
y05: 0
y06: 0
y07: 0
y08: 0
y09: 0
y10: 1
y11: 0
y12: 0
y13: 0
y14: 1
y15: 0
y16: 0
y17: 1
y18: 1
y19: 1
y20: 0
y21: 0
y22: 1
y23: 0
y24: 1
y25: 1
y26: 1
y27: 1
y28: 1
y29: 1
y30: 0
y31: 1
y32: 1
y33: 0
y34: 0
y35: 0
y36: 1
y37: 0
y38: 0
y39: 0
y40: 0
y41: 0
y42: 1
y43: 0
y44: 1

vgh OR dhk -> kfp
qpb OR tdt -> z45
njd XOR hwt -> z33
y38 AND x38 -> srk
y25 AND x25 -> sth
jrw OR tmm -> htw
qkn AND dvc -> kff
x08 AND y08 -> kmm
dcj AND wrr -> jkm
mmc XOR mdv -> z05
x35 AND y35 -> vss
x14 AND y14 -> nvj
fks OR mgs -> fww
jnh OR njq -> z24
mfk XOR pwh -> z12
rbc OR kgg -> jqw
cbm OR jjn -> nfn
x30 AND y30 -> fqm
x18 AND y18 -> kgg
x23 XOR y23 -> smg
y36 XOR x36 -> sfh
kvb AND fhp -> dhk
y24 AND x24 -> njq
x20 AND y20 -> hkt
x36 AND y36 -> dcq
y17 AND x17 -> wvs
y09 XOR x09 -> wpr
tjp OR tdk -> trq
gkq XOR qbf -> z08
fmw AND ffk -> twt
y38 XOR x38 -> ccw
vss OR nkn -> bbq
x02 AND y02 -> rfb
wwj OR pjn -> njd
csn XOR jqw -> z19
y06 XOR x06 -> fwp
tms AND wbm -> nkn
tff AND nbm -> jgd
y13 AND x13 -> vgh
y19 AND x19 -> dwn
nfn AND nsk -> jwb
smg XOR hrk -> z23
kkp AND tnm -> jnh
x03 AND y03 -> tjp
qbf AND gkq -> thk
x16 AND y16 -> gjg
mfk AND pwh -> wpw
y06 AND x06 -> jdp
x22 AND y22 -> cnp
bwv OR fwb -> mpd
mpd AND wnw -> hmk
y21 XOR x21 -> hvt
fmd XOR qcw -> z26
tcs XOR hwg -> z10
fwp AND fww -> qjk
x29 AND y29 -> nfp
cmj AND htw -> fpt
x10 AND y10 -> psb
mkr OR tqp -> fhf
bqn XOR kmr -> z15
qkq AND stj -> z20
cnp OR dbc -> hrk
vcg AND qgb -> rss
bqs OR qnq -> qbf
sth OR rss -> qcw
sfh AND bbq -> stg
stj XOR qkq -> jgb
wsq OR wvs -> hrn
y05 XOR x05 -> mdv
y27 XOR x27 -> wnw
nsm XOR mfq -> z32
njd AND hwt -> ppm
csn AND jqw -> skp
y39 AND x39 -> bnj
rkf OR hvk -> tcs
y41 XOR x41 -> nsk
hmk OR tqj -> tff
hrn XOR pfb -> z18
x32 XOR y32 -> mfq
wmj AND djn -> gsj
tnm XOR kkp -> vcg
x00 AND y00 -> mjh
srk OR rtf -> rsg
x04 XOR y04 -> hcs
y33 AND x33 -> fjr
y27 AND x27 -> tqj
psb OR pjf -> whj
jnn AND wpr -> hvk
y42 XOR x42 -> dvc
x18 XOR y18 -> pfb
x25 XOR y25 -> qgb
x03 XOR y03 -> csd
y40 XOR x40 -> qbn
kbq AND csd -> tdk
rdj AND mjh -> tqp
fhp XOR kvb -> z13
y10 XOR x10 -> hwg
x01 AND y01 -> mkr
vpc OR mqg -> wbm
csf XOR rrs -> z31
wmj XOR djn -> z37
mpd XOR wnw -> z27
fwg XOR rvj -> z07
csd XOR kbq -> z03
dwn OR skp -> stj
vfd XOR pjw -> z44
psg OR jgd -> dcj
x15 XOR y15 -> kmr
nbm XOR tff -> z28
x07 XOR y07 -> rvj
rsp AND fsf -> wsq
x16 XOR y16 -> cmj
y05 AND x05 -> mgs
y11 XOR x11 -> bcw
y40 AND x40 -> cbm
bvn OR jwb -> qkn
tkv AND npv -> wkn
grc OR jwd -> mmc
ffk XOR fmw -> z30
ghk OR grb -> pwh
x30 XOR y30 -> fmw
ppm OR fjr -> fsn
khg OR wkn -> pjw
x17 XOR y17 -> fsf
y44 XOR x44 -> vfd
x13 XOR y13 -> fhp
y28 AND x28 -> psg
pcp OR kff -> tkv
bhs XOR fsn -> z34
dvc XOR qkn -> z42
pst AND qbn -> jjn
bcw XOR whj -> z11
kmr AND bqn -> jrw
pfb AND hrn -> rbc
x37 XOR y37 -> djn
x31 AND y31 -> rrs
csf AND rrs -> pgq
tms XOR wbm -> z35
khb AND qtq -> dbc
fsn AND bhs -> vpc
y14 XOR x14 -> rvd
x22 XOR y22 -> khb
rdj XOR mjh -> z01
hvt AND bfp -> shc
rfb OR qtr -> kbq
y26 AND x26 -> bwv
y37 AND x37 -> trf
x12 AND y12 -> qcg
x23 AND y23 -> knh
qcg OR wpw -> kvb
gsj OR trf -> wqq
fmd AND qcw -> fwb
x41 AND y41 -> bvn
nsk XOR nfn -> z41
rvc OR pgq -> nsm
y32 AND x32 -> pjn
vfd AND pjw -> qpb
mfq AND nsm -> wwj
cmj XOR htw -> z16
jkm OR nfp -> ffk
x42 AND y42 -> pcp
fsf XOR rsp -> z17
rvj AND fwg -> bqs
y28 XOR x28 -> nbm
tcs AND hwg -> pjf
x08 XOR y08 -> gkq
qgb XOR vcg -> z25
hcs XOR trq -> z04
jgb OR hkt -> bfp
rvd XOR kfp -> z14
wqq AND ccw -> rtf
y20 XOR x20 -> qkq
kfp AND rvd -> qmp
x04 AND y04 -> grc
qbn XOR pst -> z40
fqm OR twt -> csf
khb XOR qtq -> z22
y00 XOR x00 -> z00
y34 AND x34 -> mqg
x11 AND y11 -> grb
y34 XOR x34 -> bhs
y09 AND x09 -> z09
hrk AND smg -> vvb
x12 XOR y12 -> mfk
gjg OR fpt -> rsp
y39 XOR x39 -> hkr
x31 XOR y31 -> rvc
kmm OR thk -> jnn
rsg XOR hkr -> z39
fht XOR fhf -> z02
hkr AND rsg -> mhh
bfp XOR hvt -> z21
shc OR nvr -> qtq
y01 XOR x01 -> rdj
trq AND hcs -> jwd
y07 AND x07 -> qnq
qmp OR nvj -> bqn
x29 XOR y29 -> wrr
y33 XOR x33 -> hwt
x19 XOR y19 -> csn
whj AND bcw -> ghk
y24 XOR x24 -> tnm
dcq OR stg -> wmj
tkv XOR npv -> z43
mhh OR bnj -> pst
mmc AND mdv -> fks
x02 XOR y02 -> fht
y44 AND x44 -> tdt
x43 AND y43 -> khg
jnn XOR wpr -> rkf
knh OR vvb -> kkp
y15 AND x15 -> tmm
x35 XOR y35 -> tms
fht AND fhf -> qtr
dcj XOR wrr -> z29
fww XOR fwp -> z06
y21 AND x21 -> nvr
y43 XOR x43 -> npv
sfh XOR bbq -> z36
qjk OR jdp -> fwg
y26 XOR x26 -> fmd
wqq XOR ccw -> z38"""

text2 = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""

def parse_input(text):
    initials, operations = text.split("\n\n")
    wire_map = {}
    operations_map = {}
    unique_wires = set()
    for i in initials.split("\n"):
        w, val = i.split(": ")
        if not w in unique_wires:
            wire_map[w] = True if val == "1" else False
            unique_wires.add(w)

    for i in operations.split("\n"):
        op, w = i.split(" -> ")
        if not w in unique_wires:
            unique_wires.add(w)
            temp_op = op.split(" ")
            operations_map[w] = (temp_op[0], "&" if temp_op[1] == "AND" else "|" if temp_op[1] == "OR" else "^", temp_op[2])

    return wire_map, operations_map


def fillout_wiremap(wire_map, operations_map):
    while True:
        updated = False

        for key, (op1, operator, op2) in operations_map.items():
            if key in wire_map:
                continue
            if op1 in wire_map and op2 in wire_map:
                if operator == '|':
                    wire_map[key] = '1' if int(wire_map[op1]) or int(wire_map[op2]) else '0'
                elif operator == '&':
                    wire_map[key] = '1' if int(wire_map[op1]) and int(wire_map[op2]) else '0'
                elif operator == '^':
                    wire_map[key] = '1' if int(wire_map[op1]) ^ int(wire_map[op2]) else '0'
                else:
                    raise ValueError(f"Unknown operator: {operator}")
                updated = True
        if not updated:
            break

    return wire_map
    
def calculate_output(text):
    wire_map, operations_map = parse_input(text)
    updated_wiremap = fillout_wiremap(wire_map, operations_map)
    keys = list(updated_wiremap.keys())
    keys.sort()
    keys = keys[::-1]
    i = 0
    binary = ""
    while keys[i][0] == "z":
        binary += updated_wiremap[keys[i]]
        i+=1
    return int(binary, 2), updated_wiremap, operations_map


ans1, solved_wiremap, operations_map = calculate_output(text)
print("answer 1: ", ans1)


def parse_input_part2(text):
    initials, operations = text.split("\n\n")
    initial_values = {}
    gate_map = {}

    for line in initials.split("\n"):
        key, value = line.split(": ")
        initial_values[key] = int(value)

    for line in operations.split("\n"):
        parts = line.split(" ")
        input1, operator, input2, _, output = parts
        gate_map[output] = (operator, input1, input2, output)

    return initial_values, gate_map

def evaluate_gate(gate, gate_map, initial_values):
    operator, input1, input2, _ = gate

    if input1 in initial_values:
        input1_value = initial_values[input1]
    else:
        input1_value = evaluate_gate(gate_map[input1], gate_map, initial_values)

    if input2 in initial_values:
        input2_value = initial_values[input2]
    else:
        input2_value = evaluate_gate(gate_map[input2], gate_map, initial_values)

    if operator == "AND":
        return input1_value & input2_value
    elif operator == "OR":
        return input1_value | input2_value
    elif operator == "XOR":
        return input1_value ^ input2_value

def evaluate_system(gate_map, initial_values):
    outputs = []
    terminal_gates = [(out, gate) for out, gate in gate_map.items() if out.startswith('z')]
    for out, terminal_gate in terminal_gates:
        p = int(out[1:])
        outputs.append((p, evaluate_gate(terminal_gate, gate_map, initial_values)))

    return sum([2**p * value for p, value in outputs])

def check_op_map(op_map, x_var, y_var, op):
    if (op, x_var, y_var) in op_map:
        return op_map[(op, x_var, y_var)]
    elif (op, y_var, x_var) in op_map:
        return op_map[(op, y_var, x_var)]
    return ""

def carry_forward_check(op_map, gate_map, num_outputs):
    carry_forward = ""
    new_carry = ""
    to_be_verified_list = []
    checked_list = []

    for i in range(num_outputs):
        index = f"%02d" % i
        x_var = f"x{index}"
        y_var = f"y{index}"
        z_var = f"z{index}"

        digit1 = check_op_map(op_map, x_var, y_var, "XOR")
        carry1 = check_op_map(op_map, x_var, y_var, "AND")

        if i == 0:
            if digit1 != z_var:
                return 0, checked_list
            checked_list.append(digit1)
            carry_forward = carry1
        else:
            digit2 = check_op_map(op_map, carry_forward, digit1, "XOR")

            if digit2 != z_var:
                return i - 1, checked_list

            checked_list.append(digit1)
            for item in to_be_verified_list:
                checked_list.append(item)

            new_carry = check_op_map(op_map, carry_forward, digit1, "AND")
            carry_forward = check_op_map(op_map, carry1, new_carry, "OR")

            to_be_verified_list.append(carry_forward)
            to_be_verified_list.append(new_carry)

    return num_outputs, checked_list

def find_swaps(gate_map):
    op_map = {}
    for out, gate in gate_map.items():
        op_map[(gate[0], gate[1], gate[2])] = out

    terminal_gates = [(out, gate) for out, gate in gate_map.items() if out.startswith('z')]
    num_outputs = len(terminal_gates)

    swaps = set()
    personal_best, checked_list = carry_forward_check(op_map, gate_map, num_outputs)

    for _ in range(4):
        for op1, op2 in combinations(gate_map.keys(), 2):
            gate1 = gate_map[op1]
            gate2 = gate_map[op2]

            if op1 in checked_list or op2 in checked_list:
                continue

            op_map[(gate1[0], gate1[1], gate1[2])] = op2
            op_map[(gate2[0], gate2[1], gate2[2])] = op1

            gate_map[op1] = gate2
            gate_map[op2] = gate1

            new_attempt, checked_in_attempt = carry_forward_check(op_map, gate_map, num_outputs)

            if new_attempt > personal_best:
                personal_best = new_attempt
                checked_list = checked_in_attempt

                swaps.add((op1, op2))
                break

            op_map[(gate1[0], gate1[1], gate1[2])] = op1
            op_map[(gate2[0], gate2[1], gate2[2])] = op2

            gate_map[op1] = gate1
            gate_map[op2] = gate2

    swaps_sorted = sorted(sum(swaps, start=tuple()))
    return ",".join(swaps_sorted)

def find_all_swaps(text):
    initial_values, gate_map = parse_input_part2(text)
    swaps = find_swaps(gate_map)
    return swaps


print("asnwer 2:", find_all_swaps(text))

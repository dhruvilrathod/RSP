text1 = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


text2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

text = """Register A: 30899381
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0"""

def parse_input(text):

    lines = text.strip().split("\n")
    reg_a = int(lines[0].split(":")[1].strip())
    reg_b = int(lines[1].split(":")[1].strip())
    reg_c = int(lines[2].split(":")[1].strip())
    program = list(map(int, lines[4].split(":")[1].strip().split(',')))
    program_text = lines[4].split(":")[1].strip()
    
    return program, reg_a, reg_b, reg_c, program_text

def run_program(program, reg_a, reg_b, reg_c):

    registers = {'A': reg_a, 'B': reg_b, 'C': reg_c}

    output = []

    ip = 0

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        else:
            raise ValueError("Invalid combo operand: 7")

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else 0

        if opcode == 0:
            denominator = 2 ** get_combo_value(operand)
            registers['A'] //= denominator

        elif opcode == 1:
            registers['B'] ^= operand

        elif opcode == 2:
            registers['B'] = get_combo_value(operand) % 8

        elif opcode == 3:
            if registers['A'] != 0:
                ip = operand
                continue

        elif opcode == 4:
            registers['B'] ^= registers['C']

        elif opcode == 5:
            output.append(get_combo_value(operand) % 8)

        elif opcode == 6:
            denominator = 2 ** get_combo_value(operand)
            registers['B'] = registers['A'] // denominator

        elif opcode == 7:
            denominator = 2 ** get_combo_value(operand)
            registers['C'] = registers['A'] // denominator

        else:
            raise ValueError(f"Invalid opcode: {opcode}")

        ip += 2

    return ",".join(map(str, output))


def solve_program(text):
    program, reg_a, reg_b, reg_c, program_text = parse_input(text)
    return run_program(program, reg_a, reg_b, reg_c)

def find_register_a(text):
    program, reg_a, reg_b, reg_c, program_text = parse_input(text)

    A = sum(7 * 8**i for i in range(len(program) - 1)) + 1

    while True:

        output = run_program(program, A, reg_b, reg_c)
        if output == program_text:
            return A

        output = [int(_) for _ in output.split(",")]

        add = 0

        for i in range(len(output) - 1, -1, -1):
            if output[i] != program[i]:
                add = 8**i
                A += add
                break

result = solve_program(text)
print("result: ", result)

reg_a = find_register_a(text)
print("reg a: ", reg_a)
#!python3


from computer import Instruction, parse_instructions, compute


INPUT = 'day23.txt'
TEST_INPUT = '''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''


def test1():
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    instructions = parse_instructions(TEST_INPUT)
    compute(instructions, registers)


def part1():
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    instructions = parse_instructions(open(INPUT, 'r').read())
    compute(instructions, registers)


def main():
    test1()


if __name__ == '__main__':
    main()
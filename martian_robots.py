import sys

DIRECTIONS = ['N', 'E', 'S', 'W']

def store_instructions(file_name):
    instructions = list()

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                instructions.append(line)
        return instructions


def move(loc,orientation):
    if orientation == 'N':
        loc = (loc[0], loc[1] + 1)
    elif orientation == 'S':
        loc = (loc[0], loc[1] - 1)
    elif orientation == 'E':
        loc = (loc[0] + 1, loc[1])
    elif orientation == 'W':
        loc = (loc[0] - 1, loc[1])
    return loc


def turn(current, direction):
    pass


def run_instructions(instructions):
    pass


if __name__ == "__main__":

    instructions_file = 'instructions.txt'
    instr_list = store_instructions(instructions_file)

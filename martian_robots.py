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
    idx = DIRECTIONS.index(current)
    if direction == 'L':
        idx = (idx - 1) % 4
    elif direction == 'R':
        idx = (idx + 1) % 4
    return DIRECTIONS[idx]


def run_instructions(instructions):
        grid_limit = list(map(int,instructions[0].split()))
    scent = set()
    
    start = 1

    while  start < len(instructions):
        start_pos = instructions[start].split()
        bot_instr = instructions[start+1].strip()
        start+=2

        x,y, orientation =int(start_pos[0]),int(start_pos[1]), start_pos[2]

        loc = (x,y)
        lost = False

        for i in range(len(bot_instr)):
            if bot_instr[i]=='F':
                next_loc = move(loc,orientation)
        
                if next_loc[0] < 0 or next_loc[1] < 0 or next_loc[0] > grid_limit[0] or next_loc[1] > grid_limit[1]:
                    if (loc[0], loc[1], orientation) in scent:
                        continue
                    else:
                        lost = True
                        scent.add((loc[0], loc[1], orientation))
                        break
                else:
                    loc = next_loc
            elif bot_instr[i] == 'L' or bot_instr[i] == 'R':
                orientation = turn(orientation, bot_instr[i])
            else:
                print(f"Invalid command '{bot_instr[i]}', skipping.")
                continue

        result = f"{loc[0]} {loc[1]} {orientation}"
        if lost:
            result += " LOST"
        print(result)


if __name__ == "__main__":

    instructions_file = 'instructions.txt'
    instr_list = store_instructions(instructions_file)
    run_instructions(instr_list)


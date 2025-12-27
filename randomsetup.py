#File that randomly generates positions for testing Setup

import random

# Rows in numbers and columns in letters
cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',"I"]

removed_positions = []

def start_position():
    edge = random.choice([cols[0],cols[-1],rows[0],rows[-1]])
    if edge in cols:
        pos= f'{random.choice(rows[1::2])}{edge}'
    else: 
        pos= f'{edge}{random.choice(cols[1::2])}'
    removed_positions.append(pos)
    return pos
    
def end_position():
    while True:
        pos = f'{random.choice(rows[1::2])}{random.choice(cols[1::2])}'
        if pos not in removed_positions:
            removed_positions.append(pos)
            break    
    return pos

def gate_zones():
    positions = []
    while positions.__len__() < 4:
        pos = f'{random.choice(rows[1::2])}{random.choice(cols[1::2])}'
        if pos not in removed_positions:
            positions.append(pos)
            removed_positions.append(pos)
    return positions

def water_bottles():
    positions = []
    while positions.__len__() < 3:
        pos = f'{random.choice(rows[1::2])}{random.choice(cols[1::2])}'
        if pos not in removed_positions:
            positions.append(pos)
            removed_positions.append(pos)
    return positions

def twoxfour():
    positions = []
    number = random.randint(1, 10)
    while positions.__len__() < number:
        pos = f'{random.choice(rows[::2])}{random.choice(cols[::2])}'
        if pos not in removed_positions:
            positions.append(pos)
            removed_positions.append(pos)
    return positions

print(f"The starting point is: \033[1m {start_position()} \033[0m \n")

print(f'''Location of Gate Zones:
    Gate A: \033[1m{(g := gate_zones())[0]}\033[0m, 
    Gate B: \033[1m{g[1]}\033[0m, 
    Gate C: \033[1m{g[2]}\033[0m, 
    Gate D: \033[1m{g[3]}\033[0m\n''')

print(f'''Location of Water Bottles:
    Bottle 1: \033[1m{(b := water_bottles())[0]}\033[0m, 
    Bottle 2: \033[1m{b[1]}\033[0m, 
    Bottle 3: \033[1m{b[2]}\033[0m\n''')

print(f'''Location of the {(z := twoxfour()).__len__()} 2x4s:
{''.join(f'    2x4 {i+1}: \033[1m{z[i]}\033[0m\n' for i in range(len(z)))}''')

print(f"The target point is: \033[1m{end_position()} \033[0m \n")



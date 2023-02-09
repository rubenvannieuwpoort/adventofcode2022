def start_pos():
    global terrain
    for y in range(0, height):
        for x in range(0, width):
            if terrain[y][x] == '.':
                return (x, y)

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

width, height = max(map(lambda x: len(x), lines[:-2])), len(lines[:-2])
terrain = list(map(lambda x: x.ljust(width), lines[:-2]))

instructions = lines[-1].replace('R', ' R ').replace('L', ' L ')


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

facing = 0
x, y = start_pos()

for command in instructions.split(' '):
    if command.isnumeric():
        steps = int(command)
        dx, dy = dirs[facing]
        for _ in range(steps):
            nx, ny = (x + dx) % width, (y + dy) % height
            while terrain[ny][nx] == ' ':
                nx, ny = (nx + dx) % width, (ny + dy) % height
            if terrain[ny][nx] == '#':
                break
            x, y = nx, ny
    elif command in 'RL':
        facing = (facing + (1 if command == 'R' else -1)) % 4
    else:
        assert False

print(1000 * (y + 1) + 4 * (x + 1) + facing)

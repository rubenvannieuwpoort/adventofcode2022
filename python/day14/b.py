width = 1000

def putat(pos, c):
    global field
    field[pos[1]] = field[pos[1]][:pos[0]] + c + field[pos[1]][pos[0]+1:]

def at(pos):
    global field
    if pos[0] >= width or pos[0] < 0: return ' '
    return field[pos[1]][pos[0]]

def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

field = [(' ' * width) for _ in range(0, 166)]

floor = 0
walls = []
for line in lines:
    walls = list(map(lambda x: eval(x), line.split(' -> ')))
    for i in range(0, len(walls) - 1):
        source = walls[i]
        target = walls[i + 1]

        floor = max(floor, source[1], target[1])

        assert source[0] < width and target[0] < width and source[1] < 166 and target[1] < 166

        direction = (sgn(target[0] - source[0]), sgn(target[1] - source[1]))

        assert (direction[0] == 0 or direction[1] == 0) and (direction[0] != 0 or direction[1] != 0)

        position = source
        while position != target:
            putat(position, '#')
            position = add(position, direction)
        putat(position, '#')

for x in range(0, width):
    putat((x, floor + 2), '#')

sands = 0
sandpos = (500, 0)
while at((500, 0)) == ' ':
    if at(add(sandpos, (0, 1))) == ' ':
        sandpos = add(sandpos, (0, 1))
    elif at(add(sandpos, (-1, 1))) == ' ':
        sandpos = add(sandpos, (-1, 1))
    elif at(add(sandpos, (1, 1))) == ' ':
        sandpos = add(sandpos, (1, 1))
    else:
        putat(sandpos, 'o')
        if sands == 74:
            a = 4
        sands += 1
        sandpos = (500, 0)

    # if sandpos[0] < 0 or sandpos[0] >= width or sandpos[1] >= 165:
    #     break

print(sands)

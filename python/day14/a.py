def putat(pos, c):
    global field
    field[pos[1]] = field[pos[1]][:pos[0]] + c + field[pos[1]][pos[0]+1:]

def at(pos):
    global field
    if pos[0] > 509 or pos[0] < 0: return ' '
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

field = [(' ' * 510) for _ in range(0, 164)]

walls = []
for line in lines:
    walls = list(map(lambda x: eval(x), line.split(' -> ')))
    for i in range(0, len(walls) - 1):
        source = walls[i]
        target = walls[i + 1]

        assert source[0] < 510 and target[0] < 510 and source[1] < 164 and target[1] < 164

        direction = (sgn(target[0] - source[0]), sgn(target[1] - source[1]))

        assert (direction[0] == 0 or direction[1] == 0) and (direction[0] != 0 or direction[1] != 0)

        position = source
        while position != target:
            putat(position, '#')
            position = add(position, direction)
        putat(position, '#')

sands = 0
sandpos = (500, 0)
while True:
    if at(add(sandpos, (0, 1))) == ' ':
        sandpos = add(sandpos, (0, 1))
    elif at(add(sandpos, (-1, 1))) == ' ':
        sandpos = add(sandpos, (-1, 1))
    elif at(add(sandpos, (1, 1))) == ' ':
        sandpos = add(sandpos, (1, 1))
    else:
        putat(sandpos, 'o')
        sands += 1
        sandpos = (500, 0)

    if sandpos[0] < 0 or sandpos[0] > 509 or sandpos[1] >= 163:
        break

print(sands)

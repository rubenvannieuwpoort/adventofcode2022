def collides(x, y, shape):
    global tower
    if x < 0 or y < 0:
        return True
    for yy in range(0, 4):
        for xx in range(0, 4):
            if (shape[yy][xx] and (x + xx > 6 or tower[y + yy][x + xx])):
                return True
    return False

def settower(x, y):
    global tower, height
    tower[y][x] = True
    height = max(height, y + 1)

def toshape(shape):
    return list(map(lambda x: list(map(lambda y: y == '#', x)), shape.split('\n')))

line = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))[0]

shapes = list(map(toshape, ['####\n    \n    \n    ', ' #  \n### \n #  \n    ', '### \n  # \n  # \n    ', '#   \n#   \n#   \n#   ', '##  \n##  \n    \n    ']))

tower = [[False] * 7 for _ in range(0, 10000)]

height = 0
x = 2
y = height + 3
s = 0
cc = 0
ss = 0
# line = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
ll = len(line)
while True:
    char = line[cc % ll]
    cc += 1

    xx = 0
    if char == '<':
        xx = -1
    if char == '>':
        xx = 1

    if not collides(x + xx, y, shapes[s]):
        x += xx
    if not collides(x, y - 1, shapes[s]):
        y -= 1
    else:
        for yy in range(0, 4):
            for xx in range(0, 4):
                if shapes[s][yy][xx]:
                    settower(x + xx, y + yy)
        s = (s + 1) % 5
        ss += 1
        if ss == 2022:
            break
        x = 2
        y = height + 3

print(height)

def viewing_distance(x, y, dir):
    global trees_2d
    global width, height
    h = trees_2d[y][x]
    xd, yd = dir
    dis = 0
    while True:
        x, y = x + xd, y + yd
        if not(0 <= x and x < width and 0 <= y and y < height):
            break
        dis += 1
        if trees_2d[y][x] >= h:
            break
    return dis

def score(x, y):
    return viewing_distance(x, y, ( 0,-1)) * viewing_distance(x, y, (-1, 0)) *\
           viewing_distance(x, y, ( 1, 0)) * viewing_distance(x, y, ( 0, 1))

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
trees_2d = list(map(lambda line: list(map(lambda y: int(y), line)), lines))

height = len(trees_2d[0])
width = len(trees_2d)

max_score = 0
for y in range(0, height):
    for x in range(0, width):
        s = score(x, y)
        if s > max_score:
            max_score = s

print(max_score)
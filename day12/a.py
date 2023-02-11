lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

width = 93
height = 41

hmap = [[0 for _ in range(0, width)] for _ in range(0, height)]
turn = [[10000 for _ in range(0, width)] for _ in range(0, height)]

start = None
end = None

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == 'S':
            assert start == None
            c = 'a'
            start = (x, y)
        elif c == 'E':
            assert end == None
            c = 'z'
            end = (x, y)
        hmap[y][x] = ord(c) - ord('a')

turn[start[1]][start[0]] = 0

while turn[end[1]][end[0]] == 10000:
    for y in range(0, height):
        for x in range(0, width):
            values = [turn[y][x]]

            if x > 0 and hmap[y][x] <= hmap[y][x - 1] + 1:
                values.append(turn[y][x - 1] + 1)
            if x < width - 1 and hmap[y][x] <= hmap[y][x + 1] + 1:
                values.append(turn[y][x + 1] + 1)
            if y > 0 and hmap[y][x] <= hmap[y - 1][x] + 1:
                values.append(turn[y - 1][x] + 1)
            if y < height - 1 and hmap[y][x] <= hmap[y + 1][x] + 1:
                values.append(turn[y + 1][x] + 1)

            turn[y][x] = min(values)

print(turn[end[1]][end[0]])
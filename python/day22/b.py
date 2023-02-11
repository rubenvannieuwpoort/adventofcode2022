# uses 6 different maps with hardcoded mappings between them
# (so it only works for my specific input)

class Map:
    def __init__(self, ix, x, y, fs):
        self.ix = ix
        self.startx, self.starty = x * mapsize, y * mapsize
        self.wallpositions = set()
        self.fs = fs

    def parse(self, lines):
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                assert ch in '#.'
                if ch == '#':
                    self.wallpositions.add((x, y))

    def walk(self, facing, x, y):
        nix, nfacing, nx, ny = self.ix, facing, x + dirs[facing][0], y + dirs[facing][1]

        if not (0 <= nx and nx < mapsize and 0 <= ny and ny < mapsize):
            (nix, nfacing, nx, ny) = self.fs[facing](nx, ny)

        if (nx, ny) in maps[nix].wallpositions:
            return self.ix, facing, x, y

        return (nix, nfacing, nx, ny)


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
instructions = lines[-1]

mapsize = 50
maps = [
    Map(0, 1, 0, [lambda x, y: (1, 0, 0, y), lambda x, y: (2, 1, x, 0), lambda x, y: (3, 0, 0, mapsize - 1 - y), lambda x, y: (5, 0, 0, x)]),
    Map(1, 2, 0, [lambda x, y: (4, 2, mapsize - 1, mapsize - 1 - y), lambda x, y: (2, 2, mapsize - 1, x), lambda x, y: (0, 2, mapsize - 1, y), lambda x, y: (5, 3, x, mapsize - 1)]),
    Map(2, 1, 1, [lambda x, y: (1, 3, y, mapsize - 1), lambda x, y: (4, 1, x, 0), lambda x, y: (3, 1, y, 0), lambda x, y: (0, 3, x, mapsize - 1)]),
    Map(3, 0, 2, [lambda x, y: (4, 0, 0, y), lambda x, y: (5, 1, x, 0), lambda x, y: (0, 0, 0, mapsize - 1 - y), lambda x, y: (2, 0, 0, x)]),
    Map(4, 1, 2, [lambda x, y: (1, 2, mapsize - 1, mapsize - 1 - y), lambda x, y: (5, 2, mapsize - 1, x), lambda x, y: (3, 2, mapsize - 1, y), lambda x, y: (2, 3, x, mapsize - 1)]),
    Map(5, 0, 3, [lambda x, y: (4, 3, y, mapsize - 1), lambda x, y: (1, 1, x, 0), lambda x, y: (0, 1, y, 0), lambda x, y: (3, 3, x, mapsize - 1)])
]

for ix, zemap in enumerate(maps):
    mapdata = list(map(lambda l: l[zemap.startx:zemap.startx+mapsize], lines[zemap.starty:zemap.starty+mapsize]))
    zemap.parse(mapdata)

instructions = instructions.replace('R', ' R ').replace('L', ' L ')

m, facing, x, y = 0, 0, 0, 0
for command in instructions.split(' '):
    if command == 'L':
        facing = (facing - 1) % 4
    elif command == 'R':
        facing = (facing + 1) % 4
    else:
        steps = int(command)
        for _ in range(0, steps):
            m, facing, x, y = maps[m].walk(facing, x, y)

print(1000 * (maps[m].starty + y + 1) + 4 * (maps[m].startx + x + 1) + facing)

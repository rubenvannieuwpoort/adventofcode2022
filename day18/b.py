def neighbours(voxel):
    x,y,z = voxel
    return [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]


def is_outside(voxel):
    global outside
    x, y, z = voxel
    return not (0 <= x and x < 20) or not (0 <= y and y < 20) or not (0 <= z < 20) or (x, y, z) in outside


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

voxels = [[[False for _ in range(0, 20)] for _ in range(0, 20)] for _ in range(0, 20)]

for line in lines:
    x,y,z = list(map(lambda x: int(x), line.split(',')))
    voxels[x][y][z] = True

assert not voxels[0][0][0]
outside = set()

added = set([(0,0,0)])
while added:
    outside.update(added)
    added = set()
    for voxel in outside:
        for (nx, ny, nz) in neighbours(voxel):
            if (0 <= nx and nx < 20 and 0 <= ny and ny < 20 and 0 <= nz and nz < 20 and not voxels[nx][ny][nz]) and (nx, ny, nz) not in outside:
                added.add((nx, ny, nz))

area = 0
for x in range(0, 20):
    for y in range(0, 20):
        for z in range(0, 20):
            if voxels[x][y][z]:
                area += len(list(filter(is_outside, neighbours((x, y, z)))))

print(area)

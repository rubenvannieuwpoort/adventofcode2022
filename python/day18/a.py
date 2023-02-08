def neighbours(voxel):
    x,y,z = voxel
    return [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

coords = set()
for line in lines:
    x,y,z = list(map(lambda x: int(x), line.split(',')))
    coords.add((x, y, z))

area = 0
for voxel in coords:
    area += len(list(filter(lambda x: x not in coords, neighbours(voxel))))

print(area)

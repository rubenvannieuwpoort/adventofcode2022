def getrange(x):
    temp = x.split('-')
    return int(temp[0]), int(temp[1])

total = 0

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
for line in lines:
    sections = line.split(',')
    left = getrange(sections[0])
    right = getrange(sections[1])
    if (left[0] <= right[0] and right[1] <= left[1]) or (right[0] <= left[0] and left[1] <= right[1]):
        total += 1

print(total)

def get_row(n):
    global cols
    return list(map(lambda x: n * cols + x, range(0, cols)))


def get_col(n):
    global rows, cols
    return list(map(lambda x: x * cols + n, range(0, rows)))


def traverse(indices):
    global visible, trees

    highest = -1
    for index in indices:
        if trees[index] > highest:
            visible[index] = True
            highest = trees[index]


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
trees_2d = list(map(lambda line: list(map(lambda y: int(y), line)), lines))

cols = len(trees_2d[0])
rows = len(trees_2d)

visible = [False] * (cols * rows)
trees = []
for row in trees_2d:
    trees += row

for r in range(0, rows):
    traverse(get_row(r))
    traverse(reversed(get_row(r)))

for c in range(0, cols):
    traverse(get_col(c))
    traverse(reversed(get_col(c)))

print(len(list(filter(lambda x: x, visible))))

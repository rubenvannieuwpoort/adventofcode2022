lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
input = list(map(lambda x: (x[0], x[2]), lines))
scoremap = {
    ('A', 'X'): 3 + 1,
    ('A', 'Y'): 6 + 2,
    ('A', 'Z'): 0 + 3,
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,
    ('C', 'X'): 6 + 1,
    ('C', 'Y'): 0 + 2,
    ('C', 'Z'): 3 + 3,
}
scores = list(map(lambda x: scoremap[x], input))
print(sum(scores))

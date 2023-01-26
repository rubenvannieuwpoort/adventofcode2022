lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
input = list(map(lambda x: (x[0], x[2]), lines))
scoremap = {
    ('A', 'X'): 0 + 3,
    ('A', 'Y'): 3 + 1,
    ('A', 'Z'): 6 + 2,
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,
    ('C', 'X'): 0 + 2,
    ('C', 'Y'): 3 + 3,
    ('C', 'Z'): 6 + 1,
}
scores = list(map(lambda x: scoremap[x], input))
print(sum(scores))

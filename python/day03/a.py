def priority(c):
    n = ord(c)

    if 65 <= n and n <= 90:
        return n - 38

    if 97 <= n <= 122:
        return n - 96

    assert False

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

sum = 0

for line in lines:
    length = len(line)
    compartiment_size = length // 2
    c1 = line[:compartiment_size]
    c2 = line[compartiment_size:]
    both = set(c1).intersection(set(c2))
    assert len(both) == 1
    sum += priority(next(iter(both)))

print(sum)
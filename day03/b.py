def priority(c):
    n = ord(c)

    if 65 <= n and n <= 90:
        return n - 38

    if 97 <= n <= 122:
        return n - 96

    assert False

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

sum = 0

line_iter = iter(lines)
while True:
    try:
        g1 = next(line_iter)
        g2 = next(line_iter)
        g3 = next(line_iter)
        common = set(g1).intersection(set(g2)).intersection(set(g3))
        sum += priority(next(iter(common)))
    except StopIteration:
        break

print(sum)
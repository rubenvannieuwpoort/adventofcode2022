def myzip(x, y):
    lx = len(x)
    ly = len(y)
    diff = lx - ly
    if diff < 0:
        x += [None] * -diff
    elif diff >0:
        y += [None] * diff
    return list(zip(x, y))


def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def compare(left, right):
    if type(left) == int and type(right) == int:
        s = sgn(left - right)
        return s

    if type(left) == list or type(right) == list:
        if type(left) == int: left = [left]
        if type(right) == int: right = [right]

        for (l, r) in myzip(left, right):
            if l == None:
                return -1
            if r == None:
                return 1
            diff = compare(l, r)
            if diff != 0:
                return diff
        return 0
    

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

line_iter = iter(lines)
sum = 0
idx = 1
while True:
    left = eval(next(line_iter))
    right = eval(next(line_iter))

    if compare(left, right) == -1:
        sum += idx

    try:
        blank = next(line_iter)
    except StopIteration:
        break
    idx += 1

print(sum)

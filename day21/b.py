from math import gcd

# main idea: instead of computing numbers, compute 4-tuples (a, b, c, d) representing expression of form (ax + b) / (cx + d)
# monkeys are represented either by such a 4-tuple (for monkeys that shout a number), or a 3-tuple of strings (left_monkey_name, operator, right_monkey_name)

# the following functions to do arithmetic on expressions of form (ax + b) / (cx + d) (represented by a 4-tuples (a, b, c, d))
# (note that these are only correct assuming that the result will never contain x^2, which is not true in general)

def simplify(a, b, c, d):
    g = gcd(a, b, c, d)
    return (a // g, b // g, c // g, d //g)

def add(a, b, c, d, A, B, C, D):
    return simplify(a * D + b * C + c * B + d * A, b * D + d * B, c * D + d * C, d * D)

def sub(a, b, c, d, A, B, C, D):
    return simplify(a * D + b * C - c * B - d * A, b * D - d * B, c * D + d * C, d * D)

def mul(a, b, c, d, A, B, C, D):
    return simplify(a * B + b * A, b * B, c * D + d * C, d * D)

def div(a, b, c, d, A, B, C, D):
    return mul(a, b, c, d, C, D, A, B)

def eq(a, b, c, d, A, B, C, D):
    return (d * B - b * D) // ((a * D + b * C) - (c * B + d * A))

def evaluate(x):
    if len(x) == 4:
        return x
    if len(x) == 3:
        operator = x[1]
        f = {'+': add, '-': sub, '*': mul, '/': div, '=': eq}[operator]
        args = evaluate(monkeys[x[0]]) + evaluate(monkeys[x[2]])
        return f(*args)

def parseexpr(str):
    return (0, int(str), 0, 1) if str.isnumeric() else tuple(str.split(' '))

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

monkeys = {}
for line in lines:
    parts = line.split(': ')
    monkeyname = parts[0]
    if monkeyname == 'humn':
        monkeys[monkeyname] = (1, 0, 0, 1)
    else:
        if monkeyname == 'root':
            parts[1] = parts[1].replace('+', '=')
        monkeys[monkeyname] = parseexpr(parts[1])

print(evaluate(monkeys['root']))

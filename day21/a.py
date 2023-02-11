def parseexpr(str):
    global monkeys
    if str.isnumeric():
        return lambda: int(str)

    parts = str.split(' ')
    assert len(parts) == 3
    assert parts[1] in ['+', '-', '*', '/']
    if parts[1] == '+':
        return lambda: monkeys[parts[0]]() + monkeys[parts[2]]()
    if parts[1] == '-':
        return lambda: monkeys[parts[0]]() - monkeys[parts[2]]()
    if parts[1] == '*':
        return lambda: monkeys[parts[0]]() * monkeys[parts[2]]()
    if parts[1] == '/':
        return lambda: monkeys[parts[0]]() // monkeys[parts[2]]()

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

monkeys = {}
for line in lines:
    parts = line.split(': ')
    monkeyname = parts[0]
    monkeys[monkeyname] = parseexpr(parts[1])

print(monkeys['root']())
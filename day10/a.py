def is_interesting(cycle):
    return cycle % 40 == 20


def end_cycle():
    global cycle, x, sum

    if is_interesting(cycle):
        signal_strength = x * cycle
        sum += signal_strength

    cycle += 1


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

x = 1
cycle = 1
sum = 0

for line in lines:
    parts = line.split(' ')
    cmd = parts[0]

    assert cmd in ['addx', 'noop']

    if cmd == 'noop':
        end_cycle()
    elif cmd == 'addx':
        end_cycle()
        end_cycle()
        x += int(parts[1])

print(sum)

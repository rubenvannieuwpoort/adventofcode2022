def should_draw(x, sx):
    return abs(x - sx) <= 1


def end_cycle():
    global cycle, x, crt
    crt += '█' if (should_draw((cycle - 1) % 40, x)) else ' '
    cycle += 1


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

x = 1
cycle = 1

row = 0
crt = []

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

print(''.join(crt[  0: 40]))
print(''.join(crt[ 40: 80]))
print(''.join(crt[ 80:120]))
print(''.join(crt[120:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:240]))

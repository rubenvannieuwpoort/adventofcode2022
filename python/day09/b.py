def is_close(x, y):
    return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1


def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

def updated(x, y):
    if not is_close(x, y):
        x = (x[0] + sgn(y[0] - x[0]),
             x[1] + sgn(y[1] - x[1]))
    return x



lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

rope_length = 10
positions = [(0, 0)] * rope_length

directions = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1) }

visited = { (0, 0) }

for line in lines:
    parts = line.split(' ')

    direction = parts[0]
    steps = int(parts[1])

    step_direction = directions[direction]

    for _ in range(0, steps):
        positions[0] = (positions[0][0] + step_direction[0], positions[0][1] + step_direction[1])
        for i in range(1, rope_length):
            positions[i] = updated(positions[i], positions[i - 1])
        visited.add(positions[rope_length - 1])


print(len(visited))

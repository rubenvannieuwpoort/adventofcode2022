def is_close(x, y):
    return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1


def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

head_position = (0, 0)
tail_position = (0, 0)

directions = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1) }

visited = { tail_position }

for line in lines:
    parts = line.split(' ')

    direction = parts[0]
    steps = int(parts[1])

    step_direction = directions[direction]

    for _ in range(0, steps):
        head_position = (head_position[0] + step_direction[0], head_position[1] + step_direction[1])
        if not is_close(head_position, tail_position):
            tail_position = (tail_position[0] + sgn(head_position[0] - tail_position[0]),
                             tail_position[1] + sgn(head_position[1] - tail_position[1]))
            visited.add(tail_position)


print(len(visited))

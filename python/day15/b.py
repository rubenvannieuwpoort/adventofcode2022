def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def positions_at_distance(pos, d):
    x, y = pos
    candidates = ([ (x + k, y - d + k) for k in range(0, d) ]
                + [ (x + d - k, y + k) for k in range(0, d) ]
                + [ (x - k, y + d - k) for k in range(0, d) ]
                + [ (x - d + k, y - k) for k in range(0, d) ])
    return candidates


def parse_coords(s):
    parts = s.split(',')
    return (int(parts[0][2:]), int(parts[1][3:]))


def can_be_distress_beacon(pos):
    global sensor_data
    if not (0 <= pos[0] and pos[0] <= 4000000 and 0 <= pos[1] and pos[1] <= 4000000):
        return False
    for (sensor_position, beacon_position) in sensor_data:
        if manhattan_distance(pos, sensor_position) <= manhattan_distance(beacon_position, sensor_position):
            return False
    return True


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

sensor_data = []
for line in lines:
    parts = line.split(':')
    sensor_coords = parse_coords(parts[0][10:])
    beacon_coords = parse_coords(parts[1][22:])
    sensor_data.append((sensor_coords, beacon_coords))

smallest_sensor_x = min(map(lambda x: x[0][0], sensor_data))
largest_sensor_x = max(map(lambda x: x[0][0], sensor_data))

largest_manhattan_dist = max(map(lambda x: manhattan_distance(x[0], x[1]), sensor_data))


y = 2000000

for (sensor_position, beacon_position) in sensor_data:
    d = manhattan_distance(sensor_position, beacon_position)
    candidates = positions_at_distance(sensor_position, d + 1)
    for candidate in candidates:
        if can_be_distress_beacon(candidate):
            print(candidate[0] * 4000000 + candidate[1])
            exit(0)

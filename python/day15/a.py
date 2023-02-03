def parse_coords(s):
    parts = s.split(',')
    return (int(parts[0][2:]), int(parts[1][3:]))


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def can_be_beacon(pos):
    global sensor_data
    for (sensor_position, beacon_position) in sensor_data:
        if beacon_position == pos:
            return True
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

min_x = smallest_sensor_x - largest_manhattan_dist
max_x = largest_sensor_x + largest_manhattan_dist

y = 2000000

count = 0
for x in range(min_x, max_x):
    if not can_be_beacon((x, y)):
        count += 1

print(count)

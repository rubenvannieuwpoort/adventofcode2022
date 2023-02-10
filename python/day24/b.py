from queue import PriorityQueue


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def addState(minute, pos):
    candidate_state = (minute + manhattan_distance(pos, endpos), -minute, pos)
    if candidate_state not in visited_states:
        visited_states.add(candidate_state)
        queue.put(candidate_state)


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
width, height = len(lines[0]), len(lines)
endpos = (width - 2, height - 2)

blizzards = []
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        assert ch in '#.<>^v'
        if ch in '#.':
            continue
        dir = { '<': (-1, 0), '>': (1, 0), '^': (0, -1) , 'v': (0, 1) }[ch]
        blizzards.append((x, y, *dir))


def find_tour_end_minute(start_position, target_position, start_minute):
    global queue, visited_states, endpos

    queue = PriorityQueue()
    visited_states = set()
    endpos = target_position

    addState(start_minute, start_position)
    while not queue.empty():
        state = queue.get()
        minute, (x, y) = -state[1], state[2]

        blizzard_positions = set((1 + (b[0] - 1 + minute * b[2]) % (width - 2), 1 + (b[1] - 1 + minute * b[3]) % (height - 2)) for b in blizzards)
        if (x, y) in blizzard_positions:
            continue

        if state[2] == endpos:
            return minute

        addState(minute + 1, (x, y))  # no move

        if x < width - 2 and 0 < y and y < height - 1:  # move right
            addState(minute + 1, (x + 1, y))
        if x > 1 and 0 < y and y < height - 1:  # move left
            addState(minute + 1, (x - 1, y))
        if y > 1:  # move up
            addState(minute + 1, (x, y - 1))
        if y < height - 2:  # move down
            addState(minute + 1, (x, y + 1))

end_of_first_tour = 1 + find_tour_end_minute((1, 0), (width - 2, height - 2), 0)  # we already know this is 305 from the first part
end_of_second_tour = 1 + find_tour_end_minute((width - 2, height - 1), (1, 1), end_of_first_tour)
end_of_third_tour = 1 + find_tour_end_minute((1, 0), (width - 2, height - 2), end_of_second_tour)

print(end_of_third_tour)

# print(1 + find_tour_length((width - 2, height - 1), (1, 1), 7))

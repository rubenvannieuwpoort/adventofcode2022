HISTORY_LENGTH = 37
MAX = 256 ** HISTORY_LENGTH
WALLS_CONSTANT = ((256**7 - 1) // 255) * MAX
OFFSET = 256 ** (HISTORY_LENGTH + 3)
WALL = 256 ** (HISTORY_LENGTH + 6)
MASK = 254 * MAX

class State:
    def __init__(self):
        self.state = MAX - 1 + WALLS_CONSTANT
        self.x = 0
        self.shape = 0
        self.height = 0

    def set_shape(self, shape):
        self.x = 2
        self.shape = shape

    def move_left(self):
        candidate_shape = self.shape << 1
        if self.x > 0 and candidate_shape & self.state == 0:
            self.shape = candidate_shape
            self.x -= 1
            return True
        return False

    def move_right(self):
        candidate_shape = self.shape >> 1
        if candidate_shape & self.state == 0:
            self.shape = candidate_shape
            self.x += 1
            return True
        return False

    def move_down(self):
        candidate_shape = self.shape >> 8
        if candidate_shape & self.state == 0:
            self.shape = candidate_shape
            return True
        self.state |= self.shape
        while self.state & MASK:
            self.state = (self.state >> 8) | WALL
            self.height += 1
        return False

    def print(self):
        temp_state = self.state
        result = ''
        while temp_state:
            line = ''
            for x in reversed(range(0, 8)):
                line += ('█' if temp_state & (1 << x) else ' ')
            result = line + '\n' + result
            temp_state >>= 8
        print(result)


direction = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))[0]
shapes = [ 0b00000000000000000000000000111100 * OFFSET, 0b00000000000100000011100000010000 * OFFSET, 0b00000000000010000000100000111000 * OFFSET, 0b00100000001000000010000000100000 * OFFSET, 0b00000000000000000011000000110000 * OFFSET ]

s = 0
t = 0
total = 0
state = State()
state.set_shape(shapes[s])

while True:
    if direction[t] == '<':
        r = state.move_left()
    if direction[t] == '>':
        r = state.move_right()

    t = (t + 1) % len(direction)

    if not state.move_down():
        s = (s + 1) % 5
        total += 1
        state.set_shape(shapes[s])
        if total == 2022:
            break

print(state.height)

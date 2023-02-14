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


class Game:
    def __init__(self):
        self.dir_id = 0
        self.shape_id = 0
        self.t = 0
        self.total_blocks = 0
        self.state = State()
        self.state.set_shape(shapes[0])

    def do_block(self):
        while True:
            if direction[self.dir_id] == '<':
                self.state.move_left()
            if direction[self.dir_id] == '>':
                self.state.move_right()

            self.dir_id = (self.dir_id + 1) % len(direction)

            if not self.state.move_down():
                break

        self.shape_id = (self.shape_id + 1) % 5
        self.total_blocks += 1
        self.state.set_shape(shapes[self.shape_id])

    def get_height(self):
        return self.state.height

    def get_state(self):
        return (self.dir_id, self.shape_id, self.state.state)


def find_cycle(tortoise, hare):
    hare.do_block()
    while tortoise.get_state() != hare.get_state():
        hare.do_block()
        hare.do_block()
        tortoise.do_block()

    cycle_length = 1
    height = hare.get_height()
    hare.do_block()
    while tortoise.get_state() != hare.get_state():
        hare.do_block()
        cycle_length += 1
    
    return hare.get_height() - height, cycle_length


num_blocks = 1000000000000
direction = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))[0]
shapes = [ 0b00000000000000000000000000111100 * OFFSET, 0b00000000000100000011100000010000 * OFFSET, 0b00000000000010000000100000111000 * OFFSET, 0b00100000001000000010000000100000 * OFFSET, 0b00000000000000000011000000110000 * OFFSET ]

hare = Game()
tortoise = Game()

height_diff, cycle_length = find_cycle(tortoise, hare)

complete_cycles = (num_blocks - hare.total_blocks) // cycle_length
hare.total_blocks += complete_cycles * cycle_length
hare.state.height += complete_cycles * height_diff

while hare.total_blocks < num_blocks:
    hare.do_block()

print(hare.get_height())

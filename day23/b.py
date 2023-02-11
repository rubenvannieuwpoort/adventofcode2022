from dataclasses import dataclass


@dataclass
class Elf:
    pos: tuple[int, int]
    proposed: tuple[int, int] = None

    def offset(self, dx, dy):
        return (self.pos[0] + dx, self.pos[1] + dy)

    def neighbours(self):
        return [self.offset(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

    def propose(self):
        if not any(nb in elf_positions for nb in self.neighbours()):
            return None
        for i in direction_index:
            if not any(self.offset(dx, dy) in elf_positions for (dx, dy) in check[i]):
                return self.offset(*directions[i])


direction_index = [0, 1, 2, 3]
check = [[(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)], [(-1, -1), (-1, 0), (-1, 1), ], [(1, -1), (1, 0), (1, 1)]]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# read elf positions
lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

height = len(lines)
width = len(lines[0])

elfs = []
for y, line in enumerate(lines):
    assert len(line) == width
    for x, ch in enumerate(line):
        assert ch in '#.'
        if ch == '#':
            elfs.append(Elf((x, y)))

round = 1
while True:
    # first half: propose
    elf_positions = set(elf.pos for elf in elfs)
    for elf in elfs:
        elf.proposed = elf.propose()

    accepted_proposals = set()
    refused_proposals = set()
    for elf in elfs:
        if elf.proposed:
            if elf.proposed not in accepted_proposals and elf.proposed not in refused_proposals:
                accepted_proposals.add(elf.proposed)
            elif elf.proposed in accepted_proposals:
                accepted_proposals.remove(elf.proposed)
                refused_proposals.add(elf.proposed)

    # second half: move
    elf_moved = False
    for elf in elfs:
        if elf.proposed and elf.proposed in accepted_proposals:
            elf.pos = elf.proposed
            elf_moved = True

    if not elf_moved:
        break

    round += 1

    # rotate preferred direction
    direction_index = direction_index[1:] + [direction_index[0]]

print(round)
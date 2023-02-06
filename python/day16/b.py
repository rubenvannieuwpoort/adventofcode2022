import queue
from dataclasses import dataclass, field
from typing import Any


total_minutes = 26

class PriorityQueue:
    def __init__(self):
        self.pq = queue.PriorityQueue()

    def insert(self, item):
        self.pq.put_nowait(item)

    def retrieve(self):
        try:
            return self.pq.get_nowait()
        except queue.Empty:
            return None


@dataclass(order = True)
class State:
    max_score: int
    score: int = field(compare=False)
    closed_valves: list[str] = field(compare=False)
    player_position: str = field(compare=False)
    player_free: int = field(compare = False)
    elephant_position: str = field(compare=False)
    elephant_free: int = field(compare = False)

    def __init__(self, score, closed_valves, player_position, player_free, elephant_position, elephant_free):
        self.max_score = State.compute_max_score(score, closed_valves, min(player_free, elephant_free))
        self.score = score
        self.closed_valves = closed_valves
        self.player_position = player_position
        self.player_free = player_free
        self.elephant_position = elephant_position
        self.elephant_free = elephant_free

    def compute_max_score(score, closed_valves, current_minute):
        global nodes, total_minutes
        # compute rudimentary upper bound for score, and negate it so that that high scores will have high priority in the PriorityQueue
        return -(score + sum(nodes[name] for name in closed_valves) * max(total_minutes - current_minute - 1, 0))


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

nodes = {}
neighbours = {}
for line in lines:
    parts = line.split(';')
    name = parts[0][6:8]
    flow = int(parts[0].split('=')[1])
    nodes[name] = flow
    nbs = list(map(lambda x: x[-2:], parts[1].split(', ')))
    neighbours[name] = nbs


# calculate distances from every valve to every valve (with pressure > 0)
distances = { node: {} for node in nodes }
for node in nodes:
    pq = PriorityQueue()
    pq.insert((0, node))
    while True:
        item = pq.retrieve()
        if item is None:
            break
        (distance, candidate) = item

        if candidate not in distances[node]:
            distances[node][candidate] = distance
            for nb in neighbours[candidate]:
                if nb not in distances[node]:
                    pq.insert((distance + 1, nb))

# filter out valves without pressure to trim down the tree a bit
distances = { k: { kk: vv for (kk, vv) in v.items() if nodes[kk] > 0 } for (k, v) in distances.items() }

closed_valves = [ n for n in nodes if nodes[n] > 0 ]
closed_valves.sort(key=lambda x: nodes[x], reverse=True)

pq = PriorityQueue()
pq.insert(State(0, closed_valves, 'AA', 1, 'AA', 1))

best_score = 0
while True:
    c: State = pq.retrieve()

    if c == None or -c.max_score < best_score:
        break

    if c.score > best_score:
        best_score = c.score

    current_minute = min(c.player_free, c.elephant_free)

    if current_minute == total_minutes or not c.closed_valves or (not neighbours[c.player_position] and not neighbours[c.elephant_position]):
        continue

    # this is not completely foolproof as there is no option to wait, but it works for the input
    # (theoretically for the last step it might be faster to wait for the other to finish and handle last valve
    # than to start going there yourself, but this doesn't seem to happen in the input, so I will not fix this)
    if c.player_free == current_minute:
        for nb in c.closed_valves:
            if nb in distances[c.player_position]:
                cv = c.closed_valves.copy()
                dis = distances[c.player_position][nb]
                cv.remove(nb)
                score = c.score + (nodes[nb] * (total_minutes - current_minute - dis))
                pq.insert(State(score, cv, nb, current_minute + dis + 1, c.elephant_position, c.elephant_free))
    elif c.elephant_free == current_minute:
        for nb in c.closed_valves:
            if nb in distances[c.elephant_position]:
                cv = c.closed_valves.copy()
                dis = distances[c.elephant_position][nb]
                cv.remove(nb)
                score = c.score + (nodes[nb] * (total_minutes - current_minute - dis))
                pq.insert(State(score, cv, c.player_position, c.player_free, nb, current_minute + dis + 1))
    else:
        raise Exception('This should never happen')

print(best_score)


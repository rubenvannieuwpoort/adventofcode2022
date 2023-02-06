from queue import PriorityQueue
from dataclasses import dataclass, field


total_minutes = 30


@dataclass(order = True)
class State:
    max_score: int
    score: int = field(compare=False)
    closed_valves: list[str] = field(compare=False)
    current_position: str = field(compare=False)
    current_minute: int = field(compare=False)

    def __init__(self, score, closed_valves, current_position, current_minute):
        self.max_score = State.compute_max_score(score, closed_valves, current_minute)
        self.score = score
        self.closed_valves = closed_valves
        self.current_position = current_position
        self.current_minute = current_minute

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


distances = { node: {} for node in nodes }
for node in nodes:
    pq = PriorityQueue()
    pq.put((0, node))
    while not pq.empty():
        item = pq.get()
        if item is None:
            break
        (distance, candidate) = item

        if candidate not in distances[node]:
            distances[node][candidate] = distance
            for nb in neighbours[candidate]:
                if nb not in distances[node]:
                    pq.put((distance + 1, nb))

# filter out valves without pressure to trim down the tree a bit
distances = { k: { kk: vv for (kk, vv) in v.items() if nodes[kk] > 0 } for (k, v) in distances.items() }

closed_valves = [ n for n in nodes if nodes[n] > 0 ]
closed_valves.sort(key=lambda x: nodes[x], reverse=True)

pq = PriorityQueue()
pq.put(State(0, closed_valves, 'AA', 1))

best_score = 0
while not pq.empty():
    c: State = pq.get()

    if -c.max_score < best_score:
        break

    if c.score > best_score:
        best_score = c.score

    if c.current_minute == total_minutes or not c.closed_valves or not neighbours[c.current_position]:
        continue

    for nb in c.closed_valves:
        if nb in distances[c.current_position]:
            cv = c.closed_valves.copy()
            dis = distances[c.current_position][nb]
            cv.remove(nb)
            score = c.score + (nodes[nb] * (total_minutes - c.current_minute - dis))
            pq.put(State(score, cv, nb, c.current_minute + dis + 1))

print(best_score)

import re
from dataclasses import dataclass
from multiprocessing import Pool
from datetime import datetime
from functools import cache


@dataclass(frozen=True, eq=True)
class Costs:
    ore_bot_cost: int
    clay_bot_cost: int
    obs_bot_cost: tuple[int, int]
    geode_bot_cost: tuple[int, int]


def nums(line):
    return list(map(lambda x: int(x), filter(lambda x: x.isdigit(), re.split(' |:', line))))


@cache
def f(costs, ore_bots, ore, clay_bots, clay, obs_bots, obs, geode_bots, geodes, minutes_left):
    assert ore >= 0 and clay >= 0 and obs >= 0 and geodes >= 0

    if minutes_left == 0:
        return geodes

    best = f(costs, ore_bots, ore + ore_bots, clay_bots, clay + clay_bots, obs_bots, obs + obs_bots, geode_bots, geodes + geode_bots, minutes_left - 1)
    if ore >= costs.ore_bot_cost:
        best = max(best, f(costs, ore_bots + 1, ore + ore_bots - costs.ore_bot_cost, clay_bots, clay + clay_bots, obs_bots, obs + obs_bots, geode_bots, geodes + geode_bots, minutes_left - 1))
    if ore >= costs.clay_bot_cost:
        best = max(best, f(costs, ore_bots, ore + ore_bots - costs.clay_bot_cost, clay_bots + 1, clay + clay_bots, obs_bots, obs + obs_bots, geode_bots, geodes + geode_bots, minutes_left - 1))
    if ore >= costs.obs_bot_cost[0] and clay >= costs.obs_bot_cost[1]:
        best = max(best, f(costs, ore_bots, ore + ore_bots - costs.obs_bot_cost[0], clay_bots, clay + clay_bots - costs.obs_bot_cost[1], obs_bots + 1, obs + obs_bots, geode_bots, geodes + geode_bots, minutes_left - 1))
    if ore >= costs.geode_bot_cost[0] and obs >= costs.geode_bot_cost[1]:
        best = max(best, f(costs, ore_bots, ore + ore_bots - costs.geode_bot_cost[0], clay_bots, clay + clay_bots, obs_bots, obs + obs_bots - costs.geode_bot_cost[1], geode_bots + 1, geodes + geode_bots, minutes_left - 1))

    return best


def compute_contract(id, ore_bot_cost, clay_bot_cost, obs_bot_cost_1, obs_bot_cost_2, geode_bot_cost_1, geode_bot_cost_2):
    costs = Costs(ore_bot_cost, clay_bot_cost, (obs_bot_cost_1, obs_bot_cost_2), (geode_bot_cost_1, geode_bot_cost_2))
    best_score = f(costs, 1, 0, 0, 0, 0, 0, 0, 0, 24)
    log(f'{id}: {best_score}')
    return id * best_score


def log(msg):
    time = datetime.now().strftime("%H:%M:%S")
    print(f'{time}: {msg}')


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

def mapfunc(t):
    return compute_contract(*t)

arguments = [tuple(nums(line)) for line in lines]
with Pool(8) as p:
   print(sum(p.map(mapfunc, arguments)))

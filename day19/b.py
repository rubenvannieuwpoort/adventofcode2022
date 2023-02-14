import re
from dataclasses import dataclass
from datetime import datetime
from functools import lru_cache, reduce


@dataclass(frozen=True, eq=True)
class Costs:
    ore_bot_cost: int
    clay_bot_cost: int
    obs_bot_cost: tuple[int, int]
    geode_bot_cost: tuple[int, int]


def nums(line):
    return list(map(lambda x: int(x), filter(lambda x: x.isdigit(), re.split(' |:', line))))


@lru_cache(maxsize=134217728)
def f(costs, ore_bots, ore, clay_bots, clay, obs_bots, obs, geodes, minutes_left):
    assert ore >= 0 and clay >= 0 and obs >= 0 and geodes >= 0

    if minutes_left == 0:
        return geodes

    best = geodes

    m, temp_ore, temp_clay, temp_obs = minutes_left, ore, clay, obs
    while m > 0 and temp_ore < costs.ore_bot_cost:
        temp_ore += ore_bots
        temp_clay += clay_bots
        temp_obs += obs_bots
        m -= 1
    if m > 0:
        best = max(best, f(costs, ore_bots + 1, temp_ore + ore_bots - costs.ore_bot_cost, clay_bots, temp_clay + clay_bots, obs_bots, temp_obs + obs_bots, geodes, m - 1))

    m, temp_ore, temp_clay, temp_obs = minutes_left, ore, clay, obs
    while m > 0 and temp_ore < costs.clay_bot_cost:
        temp_ore += ore_bots
        temp_clay += clay_bots
        temp_obs += obs_bots
        m -= 1
    if m > 0:
        best = max(best, f(costs, ore_bots, temp_ore + ore_bots - costs.clay_bot_cost, clay_bots + 1, temp_clay + clay_bots, obs_bots, temp_obs + obs_bots, geodes, m - 1))

    m, temp_ore, temp_clay, temp_obs = minutes_left, ore, clay, obs
    while m > 0 and (temp_ore < costs.obs_bot_cost[0] or temp_clay < costs.obs_bot_cost[1]):
        temp_ore += ore_bots
        temp_clay += clay_bots
        temp_obs += obs_bots
        m -= 1
    if m > 0:
        best = max(best, f(costs, ore_bots, temp_ore + ore_bots - costs.obs_bot_cost[0], clay_bots, temp_clay + clay_bots - costs.obs_bot_cost[1], obs_bots + 1, temp_obs + obs_bots, geodes, m - 1))

    m, temp_ore, temp_clay, temp_obs = minutes_left, ore, clay, obs
    while m > 0 and (temp_ore < costs.geode_bot_cost[0] or temp_obs < costs.geode_bot_cost[1]):
        temp_ore += ore_bots
        temp_clay += clay_bots
        temp_obs += obs_bots
        m -= 1
    if m > 0:
        best = max(best, f(costs, ore_bots, temp_ore + ore_bots - costs.geode_bot_cost[0], clay_bots, temp_clay + clay_bots, obs_bots, temp_obs + obs_bots - costs.geode_bot_cost[1], geodes + m - 1, m - 1))

    return best


def compute_contract(ore_bot_cost, clay_bot_cost, obs_bot_cost_1, obs_bot_cost_2, geode_bot_cost_1, geode_bot_cost_2):
    costs = Costs(ore_bot_cost, clay_bot_cost, (obs_bot_cost_1, obs_bot_cost_2), (geode_bot_cost_1, geode_bot_cost_2))
    return f(costs, 1, 0, 0, 0, 0, 0, 0, 32)


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))[0:3]

arguments = [tuple(nums(line)[1:]) for line in lines]
print(reduce(lambda x, y: x * y, map(lambda t: compute_contract(*t), arguments)))

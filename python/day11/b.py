class Monkey:
    def __init__(self, monkeys, items, value1, op, value2, divisor, truemonkey, falsemonkey):
        self.id = len(monkeys)
        self.inspected = 0
        self.monkeys = monkeys
        self.items = items
        self.value1 = value1
        self.op = op
        self.value2 = value2
        self.divisor = divisor
        self.truemonkey = truemonkey
        self.falsemonkey = falsemonkey

    def to_remainder_form(self):
        for i in range(0, len(self.items)):
            self.items[i] = self.reduce([self.items[i]] * len(self.monkeys))

    def reduce(self, remainders):
        assert len(remainders) == len(self.monkeys)
        for i in range(0, len(remainders)):
            remainders[i] = remainders[i] % self.monkeys[i].divisor
        return remainders

    def evalval(self, old, x):
        if x == 'old':
            return old
        return [int(x)] * len(self.monkeys)

    def evaluate(self, oldvalue, v1, op, v2):
        iv1 = self.evalval(oldvalue, v1)
        iv2 = self.evalval(oldvalue, v2)

        assert op in ['*', '+']

        if op == '*':
            return self.reduce([iv1[i] * iv2[i] for i in range(0, len(iv1))])
        else:
            return self.reduce([iv1[i] + iv2[i] for i in range(0, len(iv1))])

    def accept(self, item):
        self.items.append(item)

    def do_round(self):
        while len(self.items):
            item = self.items.pop(0)
            self.inspected += 1
            item = self.evaluate(item, self.value1, self.op, self.value2)
            if item[self.id] == 0:
                self.monkeys[self.truemonkey].items.append(item)
            else:
                self.monkeys[self.falsemonkey].items.append(item)


def parse_monkey(line_iter, monkeys):
    next(line_iter)
    items = list(map(lambda x: int(x), next(line_iter)[18:].split(', ')))
    expr = next(line_iter)[19:].split(' ')
    value1 = expr[0]
    op = expr[1]
    value2 = expr[2]
    divisor = int(next(line_iter)[21:])
    truemonkey = int(next(line_iter)[29:])
    falsemonkey = int(next(line_iter)[30:])

    try:
        next(line_iter)
    except StopIteration:
        pass

    return Monkey(monkeys, items, value1, op, value2, divisor, truemonkey, falsemonkey)


def do_round(monkeys):
    for monkey in monkeys:
        monkey.do_round()
    

nr_monkeys = 8
rounds = 10000


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
line_iter = iter(lines)
monkeys = []

for _ in range(0, nr_monkeys):
    monkeys.append(parse_monkey(line_iter, monkeys))

for monkey in monkeys:
    monkey.to_remainder_form()

for _ in range(0, 10000):
    do_round(monkeys)

sorted_inspects = list(reversed(sorted(list(map(lambda x: x.inspected, monkeys)))))
print(sorted_inspects[0] * sorted_inspects[1])

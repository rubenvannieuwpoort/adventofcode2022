class myzip:
    def __init__(self, left, right):
        self.left_ended = False
        self.left_iter = iter(left)
        self.right_ended = False
        self.right_iter = iter(right)

    def __iter__(self):
        return self

    def get_left_val(self):
        if self.left_ended: return None
        try:
            return next(self.left_iter)
        except StopIteration:
            self.left_ended = True
            return None

    def get_right_val(self):
        if self.right_ended: return None
        try:
            return next(self.right_iter)
        except StopIteration:
            self.right_ended = True
            return None

    def __next__(self):
        left = self.get_left_val()
        right = self.get_right_val()

        if self.left_ended and self.right_ended:
            raise StopIteration

        return (left, right)


def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def compare(left, right):
    if type(left) == int and type(right) == int:
        s = sgn(left - right)
        return s

    if type(left) == list or type(right) == list:
        if type(left) == int: left = [left]
        if type(right) == int: right = [right]

        for (l, r) in myzip(left, right):
            if l == None:
                return -1
            if r == None:
                return 1
            diff = compare(l, r)
            if diff != 0:
                return diff
        return 0
    

items = list(map(lambda x: eval(x), filter(lambda x: x != '', map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))))
sorted_items = [ [[2]], [[6]] ]

while len(items) > 0:
    item = items.pop(0)

    ii = 0
    for i in range(0, len(sorted_items)):
        if compare(item, sorted_items[i]) < 0:
            break
        ii = i + 1
            

    sorted_items = sorted_items[:ii] + [item] + sorted_items[ii:]

print((sorted_items.index([[2]]) + 1) * (sorted_items.index([[6]]) + 1))
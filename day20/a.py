from dataclasses import dataclass

@dataclass
class Node:
    value: int
    prev: 'Node'
    next: 'Node'

nums = list(map(lambda x: int(x.rstrip()), open('input.txt', 'r').readlines()))
length = len(nums)

nodes = []
for num in nums:
    nodes.append(Node(num, None, None))

for i, node in enumerate(nodes):
    node.prev = nodes[(i - 1) % length]
    node.next = nodes[(i + 1) % length]

for node in nodes:
    steps = node.value % (length - 1)

    if steps:
        n = node
        n.prev.next = n.next
        n.next.prev = n.prev
        for _ in range(0, steps):
            n = n.next

        newnext = n.next
        n.next = node
        node.prev = n
        node.next = newnext
        newnext.prev = node


n = list(filter(lambda x: x.value == 0, nodes))[0]
sum = 0

for _ in range(0, 3):
    for _ in range(0, 1000):
        n = n.next
    sum += n.value

print(sum)

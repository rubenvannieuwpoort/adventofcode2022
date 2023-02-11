def split(list):
    acc = []
    result = []
    for l in list:
        if l != '':
            acc.append(l)
        else:
            result.append(acc)
            acc = []
    return result


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))
by_elf = list(map(lambda x: sum(x), list(map(lambda y: list(map(lambda x: int(x), y)), split(lines)))))
print(max(by_elf))

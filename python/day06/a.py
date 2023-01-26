def is_all_different(input):
    return len(set(input)) == len(input)

def marker(input):
    holder = input[:4]
    input = input[4:]
    cnt = 4
    for c in input:
        if is_all_different(holder):
            return cnt
        holder = holder[1:] + c
        cnt += 1


line = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))[0]
print(marker(line))

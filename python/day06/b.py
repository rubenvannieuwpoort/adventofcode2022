def is_all_different(input):
    return len(set(input)) == len(input)

def marker(input):
    holder = input[:14]
    input = input[14:]
    cnt = 14
    for c in input:
        if is_all_different(holder):
            return cnt
        holder = holder[1:] + c
        cnt += 1


line = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))[0]
print(marker(line))

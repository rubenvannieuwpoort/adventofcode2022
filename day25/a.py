def from_snafu(x):
    return sum(map(lambda x: 5**x[0] * {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}[x[1]], enumerate(reversed(x))))

def to_snafu(x):
    result = ''
    while x:
        digit = x % 5
        if digit > 2:
            digit -= 5
        x -= digit
        x = x // 5
        result += '=-012'[digit + 2]
    return result[::-1]

lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

print(to_snafu(sum(map(lambda x: from_snafu(x), lines))))

def parse_command(cmd):
    cmd = cmd[5:]
    things = cmd.split(' from ')
    morethings = things[1].split(' to ')
    return (int(things[0]), int(morethings[0]), int(morethings[1]))

config = ["TFVZCWSQ", "BRQ", "SMPQTZB", "HQRFVD", "PTSBDLGJ", "ZTRW", "JRFSNMQH", "WHFNR", "BRPQTZJ"]


def move(num, src, dest):
    global config
    assert len(config[src - 1]) >= num

    taken = config[src - 1][0:num]
    config[src - 1] = config[src - 1][num:]
    config[dest - 1] = taken + config[dest - 1]


lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

for line in lines:
    (num, src, dest) = parse_command(line)
    move(num, src, dest)

result = ""
for thing in config:
    result += thing[0]

print(result)

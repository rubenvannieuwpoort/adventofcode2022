lines = list(map(lambda x: x.rstrip(), open('input.txt', 'r').readlines()))

current_dir = []

line_iter = iter(lines)

structure = {}

def get(path, structure):
    while len(path) > 0:
        structure = structure[path[0]]
        path = path[1:]
    return structure


smallest_sufficient_folder_size = 10000000000

def size(s):
    global smallest_sufficient_folder_size
    assert isinstance(s, int) or isinstance(s, dict)

    if isinstance(s, int):
        return s

    if isinstance(s, dict):
        foldersize = 0
        for ss in s:
            foldersize += size(s[ss])

        # this constant is the space we need to free, computed as 30000000 - (70000000 - total_used)
        if foldersize >= 4125990 and foldersize < smallest_sufficient_folder_size:
            smallest_sufficient_folder_size = foldersize
        
        return foldersize



line = next(line_iter)

while True:
    try:
        if line[0] == '$':
            rest = line[2:]
            cmd = rest.split(' ')[0]
            if cmd == 'cd':
                arg = rest[3:]
                if arg == '..':
                    current_dir = current_dir[:-1]
                else:
                    current_dir.append(arg)
                line = next(line_iter)
            elif cmd == 'ls':
                assert line == '$ ls'

                curstruct = get(current_dir, structure)

                line = next(line_iter)
                while line[0] != '$':
                    stuff = line.split(' ')
                    assert len(stuff) == 2
                    name = stuff[1]
                    if stuff[0] == 'dir':
                        curstruct[name] = {}
                    else:
                        curstruct[name] = int(stuff[0])
                    line = next(line_iter)
    except StopIteration:
        break

size(structure)
print(smallest_sufficient_folder_size)
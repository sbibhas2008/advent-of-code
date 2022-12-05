from collections import defaultdict
import re

with open('input.txt', 'r') as f:
    input = f.read()

[stacks, procedure] = input.split('\n\n')

split_stacks = stacks.split('\n')
indices = split_stacks[-1]
vals = split_stacks[:-1]
stacks = [int(item) for item in indices.split(' ') if item != '']

lookup = defaultdict(list)
for line in vals:
    counter = 0
    line = line.replace(' '*4, 'X')
    line = re.sub(r'\W+', '', line)
    for idx, container in enumerate(list(line)):
        if container != 'X':
            lookup[idx+1].append(container)


# cleanup
for k,v in lookup.items():
    lookup[k] = list(filter(lambda x: bool(x), v))

# list of tuples
instuctions = []
for line in procedure.split('\n'):
    line_split = line.split(' ')
    instuctions.append((line_split[1], line_split[3], line_split[5]))

# mutates the lookup
def move_crates(part):
    for inst in instuctions:
        inst = list(map(lambda x: int(x), inst))
        q, f, t = inst
        # add
        if part == 1:
            res = list(reversed(lookup[f][:q])) + lookup[t]
        else:
            res = list(lookup[f][:q]) + lookup[t]
        lookup[t] = res
        # delete
        del lookup[f][:q]
    answer = [item[1][0] for item in sorted(lookup.items())]
    return ''.join(answer)

part_1 = move_crates(1)
part_2 = move_crates(2)

print('Part 1 ->', part_1)
print('Part 2 ->', part_2)




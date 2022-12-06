with open('input.txt', 'r') as f:
    input = f.read()

input = list(input)

def solve(step):
    for i in range(len(input) - step):
        substr = input[i:i+step]
        if len(set(substr)) == step:
            return i+step

print('Part 1 - ', solve(4))
print('Part 2 - ', solve(14))

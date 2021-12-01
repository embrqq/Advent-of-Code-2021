
inp = open("input.txt", "r")

increasing = 0
previous = None
for line in inp:
    depth = int(line)
    if previous is not None and previous < depth:
        increasing += 1

    previous = depth

print(increasing)
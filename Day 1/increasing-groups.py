inp = open("input.txt", "r")

increasing = 0
depths = []

for line in inp:
    depths.append(int(line))

previous = None
for i in range(0, len(depths)-2):

    val = depths[i] + depths[i+1] + depths[i+2]
    if previous is not None and previous < val:
        increasing += 1
    previous = val

print(increasing)

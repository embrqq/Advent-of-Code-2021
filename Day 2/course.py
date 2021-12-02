def problem1() -> int:
    inp = open("input.txt", "r")
    depth = 0
    horiz = 0
    for line in inp:
        command = line.split()
        movement = int(command[1])
        command = command[0]
        if command == "down":
            depth += movement

        elif command == "up":
            depth -= movement

        elif command == "forward":
            horiz += movement

    return depth * horiz

def problem2() -> int:
    inp = open("input.txt", "r")
    depth = 0
    horiz = 0
    aim = 0
    for line in inp:
        command = line.split()
        movement = int(command[1])
        command = command[0]
        if command == "down":
            aim += movement

        elif command == "up":
            aim -= movement

        elif command == "forward":
            
            horiz += movement
            depth += aim * movement

    return depth * horiz

    
print(problem1())
from typing import List

filename = "input.txt"

def getData():

    inp = open(filename, "r")

    data = []
    for line in inp:
        data.append(line.strip())

    inp.close()
    return data

def checkLine(line: str) -> int:

    stack = []

    for char in line:
        if char in ["(", "{", "[", "<"]:
            stack.append(char)
        else:
            if char == ")":
                if not (stack.pop() == "("):
                    return 3
            if char == "]":
                if not (stack.pop() == "["):
                    return 57
            if char == "}":
                if not (stack.pop() == "{"):
                    return 1197
            if char == ">":
                if not (stack.pop() == "<"):
                    return 25137
    
    return 0

def completeLine(line: str) -> int:

    stack = []

    for char in line:
        if char in ["(", "{", "[", "<"]:
            stack.append(char)
        else:
            stack.pop()
    
    points = 0
    for i in range(len(stack)):
        char = stack[len(stack)-(i+1)]
        points = points * 5
        if char == "(":
            points = points + 1
        elif char == "[":
            points = points + 2
        elif char == "{":
            points = points + 3
        else:
            points = points + 4

    return points


def countPointsCorrupt(data) -> int:

    points = 0
    for line in data:
        points = points + checkLine(line)
    
    return points

def countPointsComplete(data) -> int:

    points = []
    for line in data:
        if checkLine(line) > 0:
            continue
        points.append(completeLine(line))

    points.sort()

    return points[len(points)//2]


data = getData()
print("The total syntax score is {}.".format(countPointsCorrupt(data)))
print("The total complete score is {}.".format(countPointsComplete(data)))
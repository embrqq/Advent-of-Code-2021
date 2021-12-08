from typing import List

zero = [1, 1, 1, 0, 1, 1, 1]
one = [0, 0, 1, 0, 0, 1, 0]
two = [1, 0, 1, 1, 1, 0, 1]
three = [1, 0, 1, 1, 0, 1, 1]
four = [0, 1, 1, 1, 0, 1, 0]
five = [1, 1, 0, 1, 0, 1, 1]
six = [1, 1, 0, 1, 1, 1, 1]
seven = [1, 0, 1, 0, 0, 1, 0]
eight = [1, 1, 1, 1, 1, 1, 1]
nine = [1, 1, 1, 1, 0, 1, 1]

def getData() -> List[str]:

    inp = open("input.txt", "r")

    data = []

    for line in inp:
        data.append(line.strip())

    return data

def filterMapping(mapping: str, signal: str) -> str:

    if mapping == "":
        return signal

    newMapping = ""

    for char in signal:
        if char in mapping:
            newMapping += char

    return newMapping

def countSharedWires(mappings: List[str], segments: List[int], signal: str) -> int:

    wires = 0

    for char in signal:
        i = 0
        while i < 7:
            if segments[i] == 1 and char in mappings[i]:
                wires += 1
                break
            i += 1

    return wires

def matchWirings(line: str) -> int:

    line = line.split(" | ")
    signals = line[0].split()
    numbers = line[1].split()

    mappings = [""] * 7

    # Fill in the uniques mappings
    for signal in signals:

        segments = None

        length = len(signal)

        if length  == 2:
            segments = one
        elif length == 3:
            segments = seven
        elif length == 4:
            segments = four
        elif length == 7:
            segments = eight
        else:
            continue

        for i in range(0, 7):
            if segments[i] == 1:
                mappings[i] = filterMapping(mappings[i], signal)

    
    output = ""

    for signal in numbers:
        length = len(signal)

        if length  == 2:
            output += "1"
        elif length == 3:
            output += "7"
        elif length == 4:
            output += "4"
        elif length == 7:
            output += "8"
        elif length == 6:
            if not (countSharedWires(mappings, one, signal) == 2):
                output += "6"
            elif not (countSharedWires(mappings, four, signal) == 4):
                output += "0"
            else:
                output += "9"
        elif length == 5:
            if countSharedWires(mappings, one, signal) == 2:
                output += "3"
            elif countSharedWires(mappings, four, signal) == 3:
                output += "5"
            else:
                output += "2"
    
    return int(output)

def countUniquesInOutput(data: List[str]) -> int:

    count = 0

    for line in data:
        output = line.split(" | ")[1]
        for signal in output.split():

            length = len(signal)

            if length == 2 or length == 4 or length == 3 or length == 7:
                count += 1

    return count

def sumOutputs(data: List[str]) -> int:

    total = 0

    for line in data:
        total += matchWirings(line)

    return total

data = getData()
print(countUniquesInOutput(data))
print(sumOutputs(data))
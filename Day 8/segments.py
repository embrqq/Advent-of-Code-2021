from typing import List

def getData() -> List[str]:
    inp = open("input.txt", "r")
    data = []
    for line in inp:
        data.append(line.strip())

    return data

def countSharedWires(signal1: str, signal2: str) -> int:
    wires = 0
    for char in signal1:
        if char in signal2:
            wires += 1

    return wires

def matchWirings(line: str) -> int:
    line = line.split(" | ")
    signals = line[0].split()
    numbers = line[1].split()

    one = ""
    four = ""

    for signal in signals:
        length = len(signal)

        if length  == 2:
            one = signal
        elif length == 4:
            four = signal
    
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
            if not (countSharedWires(one, signal) == 2):
                output += "6"
            elif not (countSharedWires(four, signal) == 4):
                output += "0"
            else:
                output += "9"
        elif length == 5:
            if countSharedWires(one, signal) == 2:
                output += "3"
            elif countSharedWires(four, signal) == 3:
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
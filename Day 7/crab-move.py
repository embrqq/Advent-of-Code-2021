from typing import List
def getData() -> List[int]:

    inp = open("input.txt", "r")

    data = inp.readline().strip().split(",")

    for i in range(0, len(data)):
        data[i] = int(data[i])

    return data


def getFuel(data: List[int]) -> int:

    minFuel = None

    for i in range(min(data), max(data)):

        fuel = 0
        for val in data:
            fuel += abs(val - i)

        if minFuel is None or fuel < minFuel:
            minFuel = fuel

    return minFuel

def getFuel2(data: List[int]) -> int:

    minFuel = None

    for i in range(min(data), max(data)):

        fuel = 0

        for val in data:
            dist = abs(val - i)
            fuel += (dist * (dist+1)) // 2

        if minFuel is None or fuel < minFuel:
            minFuel = fuel
    
    return minFuel

data = getData()
print(getFuel(data))
print(getFuel2(data))
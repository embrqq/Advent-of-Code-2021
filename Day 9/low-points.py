from typing import List

def getData() -> List[str]:
    inp = open("input.txt", "r")
    data = []
    for line in inp:
        data.append(line.strip())

    inp.close()

    return data

def findLows(data: List[str]) -> int:

    risk = 0

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):

            if (i - 1) >= 0 and data[i-1][j] <= data[i][j]:
                continue
            if (i + 1) < len(data) and data[i+1][j] <= data[i][j]:
                continue
            if (j - 1) >= 0 and data[i][j-1] <= data[i][j]:
                continue
            if (j + 1) < len(data[i]) and data[i][j+1] <= data[i][j]:
                continue

            risk += 1 + int(data[i][j])

    return risk

def findBasin(row: int, col: int, flags: List[List[bool]], data: List[str]) -> int:

    if flags[row][col] or data[row][col] == "9":
        return 0

    children = 0
    flags[row][col] = True

    if (row - 1) >= 0 and data[row-1][col] > data[row][col]:
        children += findBasin(row-1, col, flags, data)
    if (row + 1) < len(data) and data[row+1][col] > data[row][col]:
        children += findBasin(row+1, col, flags, data)
    if (col - 1) >= 0 and data[row][col-1] > data[row][col]:
        children += findBasin(row, col-1, flags, data)
    if (col + 1) < len(data[row]) and data[row][col+1] > data[row][col]:
        children += findBasin(row, col+1, flags, data)


    return 1 + children


def findBasins(data: List[str]) -> int:

    flags = []
    basins = []
    for i in range(0, len(data)):
        row = [False] * len(data[0])
        flags.append(row)

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):

            if (i - 1) >= 0 and data[i-1][j] <= data[i][j]:
                continue
            if (i + 1) < len(data) and data[i+1][j] <= data[i][j]:
                continue
            if (j - 1) >= 0 and data[i][j-1] <= data[i][j]:
                continue
            if (j + 1) < len(data[i]) and data[i][j+1] <= data[i][j]:
                continue

            # Is a basin:
            basins.append(findBasin(i, j, flags, data))

    basins.sort()
    length = len(basins)
    return basins[length-1] * basins[length - 2] * basins[length - 3]

data = getData()
print(findLows(data))
print(findBasins(data))

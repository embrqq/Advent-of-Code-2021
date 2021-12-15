from typing import List

filename = "input.txt"
n = 100

def getData():

    inp = open(filename, "r")

    data = []
    for line in inp:
        line = line.strip()
        row = [0] * len(line)
        for i in range(len(line)):
            row[i] = int(line[i])
        data.append(row)

    inp.close()
    return data

def flash(grid: List[List[int]], row: int, col: int) -> int:

    flashes = 1

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            if row + dr < 0 or row + dr >= len(grid):
                continue
            if col + dc < 0 or col + dc >= len(grid[0]):
                continue

            grid[row + dr][col + dc] = grid[row + dr][col + dc] + 1
            if grid[row + dr][col + dc] == 10:
                flashes = flashes + flash(grid, row + dr, col + dc)

    return flashes


def countFlashes(grid: List[List[int]], n: int) -> int:
    flashes = 0

    for iter in range(n):

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = grid[i][j] + 1

                if grid[i][j] == 10:
                    flashes = flashes + flash(grid, i, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    grid[i][j] = 0

    return flashes

def findAllFlashing(grid: List[List[int]]) -> int:

    flashes = 0
    iter = 0
    while not (flashes == (len(grid) * len(grid[0]))):
        iter = iter + 1
        flashes = countFlashes(grid, 1)
    return iter


print("There were {} flashes in {} iterations.".format(countFlashes(getData(), n), n))
print("All synchronize on iteration {}.".format(findAllFlashing(getData())))
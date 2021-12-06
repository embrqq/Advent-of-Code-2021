from typing import List

def getData():

    inp = open("input.txt", "r")

    data = []

    for line in inp:
        line = line.strip().split(" -> ")
        start = line[0].split(",")
        end = line[1].split(",")

        start = [int(start[0]), int(start[1])]
        end = [int(end[0]), int(end[1])]

        data.append([start,end])

    return data

def plotStraight(data: List[List[List[int]]], grid: List[List[int]]):

    for line in data:

        start = line[0]
        end = line[1]

        # If it is vertical
        if start[0] == end[0]:

            delta = -1

            if start[1] < end[1]:
                delta = 1

            for i in range(0, abs(start[1]-end[1])+1):

                grid[start[1] + (delta*i)][start[0]] += 1

        elif start[1] == end[1]:

            delta = -1

            if start[0] < end[0]:
                delta = 1

            for i in range(0, abs(start[0]-end[0])+1):

                grid[start[1]][start[0] + (delta*i)] += 1

    return grid

def plotDiag(data: List[List[List[int]]], grid: List[List[int]]):

    for line in data:

        start = line[0]
        end = line[1]

        if abs(start[0] - end[0]) == abs(start[1] - end[1]):

            deltax = -1
            deltay = -1

            if start[0] < end[0]:
                deltax = 1
            
            if start[1] < end[1]:
                deltay = 1

            for i in range(0, abs(start[0]-end[0]) + 1):

                grid[start[1] + (i * deltay)][start[0] + (i * deltax)] += 1

def count(grid: List[List[int]]) -> int:

    points = 0

    for row in grid:
        for val in row:
            if val >= 2:
                points += 1

    return points

def makeGrid(n: int) -> List[List[int]]:
    grid = []

    for i in range(0, n):
        row = [0] * n
        grid.append(row)

    return grid

data = getData()
grid = makeGrid(1000)

plotStraight(data, grid)
plotDiag(data, grid)

print(count(grid))

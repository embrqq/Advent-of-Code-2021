from queue import PriorityQueue
from typing import List

filename = "input.txt"

class Node:

    def __init__(self, row, col, dist, previous):
        self.row = row
        self.col = col
        self.dist = dist
        self.previous = previous

    def __lt__(self, other):
        return self.dist < other.dist

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

def dijkstra(grid: List[List[int]]) -> int:

    pq = PriorityQueue()

    flags = []
    for j in grid:
        row = [False] * len(j)
        flags.append(row)

    pq.put(Node(0, 0, 0, None))

    while not pq.empty():

        node = pq.get()
        dist = node.dist
        if flags[node.row][node.col]:
            continue
        else:
            flags[node.row][node.col] = True

        if node.row == len(grid)-1 and node.col == len(grid[0])-1:
            return dist

        for dr in range(-1, 2):
            row = node.row + dr
            col = node.col
            if row < 0 or row >= len(grid):
                continue    
            pq.put(Node(row, col, dist + grid[row][col], node))

        for dc in range(-1, 2):
            row = node.row
            col = node.col + dc
            if col < 0 or col >= len(grid[0]):
                continue
            pq.put(Node(row, col, dist + grid[row][col], node))


    return -1

def expandMap(grid: List[List[int]]) -> List[List[int]]:

    expanded = []

    for row in range(0, 5*len(grid)):
        col = [0] * (5 * len(grid[0]))
        expanded.append(col)

    for dr in range(0, 5):
        rowOffset = dr * len(grid)
        for dc in range(0, 5):
            colOffset = dc * len(grid[0])

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    expanded[rowOffset+i][colOffset+j] = 1 + ((grid[i][j] - 1 + dr + dc) % 9) 

    return expanded



grid = getData()
expanded = expandMap(grid)

print("The shortest path is of risk {} for the small map.".format(dijkstra(grid)))
print("The shortest path is of risk {} for the expanded map.".format(dijkstra(expanded)))
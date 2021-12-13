from typing import List


LARGE = 1
SMALL = 0
fileName = "input.txt"

def getCaves() -> List[str]:
    inp = open(fileName, "r")
    caves = []

    for line in inp:
        line = line.strip().split("-")

        for cave in line:
            if not (cave in caves):
                caves.append(cave)

    inp.close()

    return caves

def getGraph(caves: List[str]) -> List[List[int]]:
    inp = open(fileName, "r")
    graph = []

    for i in range(0, len(caves)):
        row = [0] * len(caves)
        graph.append(row)

        if caves[i].isupper():
            graph[i][i] = LARGE
        else:
            graph[i][i] = SMALL

    for edge in inp:
        edge = edge.strip().split("-")

        graph[caves.index(edge[0])][caves.index(edge[1])] = 1
        graph[caves.index(edge[1])][caves.index(edge[0])] = 1

        
    inp.close()
    return graph

def paths(graph: List[List[int]], caves: List[str], flags: List[bool], node: int) -> int:
    if node == caves.index("end"):
        return 1
    if flags[node]:
        return 0
    if graph[node][node] == SMALL:
        flags[node] = True

    count = 0
    for i in range(len(graph[node])):
        if i == node:
            continue
        if graph[node][i] == 1:
            count += paths(graph, caves, flags, i)

    flags[node] = False

    return count


def doublePaths(graph: List[List[int]], caves: List[str], flags: List[bool], node: int, doubled: bool) -> int:
    setDoubled = False
    if node == caves.index("end"):
        return 1
    if flags[node]:
        if node == caves.index("start") or doubled:
            return 0
        else:
            doubled = True
            setDoubled = True
    
    if graph[node][node] == SMALL:
        flags[node] = True

    count = 0
    for i in range(len(graph[node])):
        if i == node:
            continue
        if graph[node][i] == 1:
            count += doublePaths(graph, caves, flags, i, doubled)

    if not setDoubled:
        flags[node] = False

    return count

caves = getCaves()
graph = getGraph(caves)
flags = [False] * len(caves)

for i in range(len(graph)):

    print("{:5s} : {}".format(caves[i], graph[i]))

count = paths(graph, caves, flags, caves.index("start"))
print("There are {} possible paths in the graph visiting small caves once.".format(count))

countDouble = doublePaths(graph, caves, flags, caves.index("start"), False)
print("There are {} possible paths in the graph where one small cave is visited twice.".format(countDouble))
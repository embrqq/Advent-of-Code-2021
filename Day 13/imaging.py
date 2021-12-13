from typing import List

fileName = "input.txt"

def getData():
    inp = open(fileName, "r")

    points = []
    rows = 0
    cols = 0

    line = inp.readline().strip()
    while not (line == ""):
        coords = line.split(",")
        coords[0] = int(coords[0])
        coords[1] = int(coords[1])

        rows = max(rows, coords[1])
        cols = max(cols, coords[0])

        points.append(coords)
        line = inp.readline().strip()

    folds = []

    for line in inp:
        line = line.strip()
        line = line.strip("fold along ")
        fold = line.split("=")
        fold[1] = int(fold[1])
        folds.append(fold)

    inp.close()
    return points, folds, 1+rows, 1+cols

def plotPoints(points: List[List[int]], rows: int, cols: int) -> List[List[bool]]:
    plot = []
    for i in range(0, rows):
        row = [False] * cols
        plot.append(row)

    for point in points:
        col = point[0]
        row = point[1]
        plot[row][col] = True

    return plot

def fold(plot: List[List[bool]], fold):
    rows = len(plot)
    cols = len(plot[0])

    # Fold along horizontal line
    if fold[0] == "y":

        row = fold[1]
        delta = 1
        while (row+delta) < rows and (row-delta) >= 0:
            for i in range(0, cols):
                plot[row-delta][i] = plot[row-delta][i] or plot[row+delta][i]

            delta = delta+1
        
        plot = plot[:row]

    else:

        col = fold[1]
        delta = 1
        while (col+delta) < cols and (col-delta) >= 0:
            for i in range(0, rows):
                plot[i][col-delta] = plot[i][col-delta] or plot[i][col+delta]

            delta = delta+1

        for i in range(0, rows):
            plot[i] = plot[i][:col]

    return plot

def countDots(plot: List[List[bool]]):
    dots = 0
    for row in plot:
        for val in row:
            if val:
                dots = dots + 1
    return dots

def printPlot(plot: List[List[bool]]):
    for row in plot:
        for val in row:
            if val:
                print("#", end="")
            else:
                print(".", end="")
        print()

def allFolds(plot: List[List[bool]], folds):
    for fo in folds:
        plot = fold(plot, fo)

    return plot

def problem1():
    points, folds, rows, cols = getData()
    plot = plotPoints(points, rows, cols)
    plot = fold(plot, folds[0])
    dots = countDots(plot)
    print("There are {} dots visible.".format(dots))

def problem2():
    points, folds, rows, cols = getData()
    plot = plotPoints(points, rows, cols)
    plot = allFolds(plot, folds)
    printPlot(plot)

problem1()
problem2()
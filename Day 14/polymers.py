from typing import List

filename = "input.txt"

def getData():

    inp = open(filename, "r")

    polymer = inp.readline().strip()
    inp.readline()

    table = {}

    for line in inp:
        line = line.strip().split(" -> ")
        table[line[0]] = line[1]

    return polymer, table

def insertions(polymer: str, table: dict, n: int) -> dict:

    pairs = {}
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        pairs[pair] = pairs.get(pair, 0) + 1

    for iter in range(n):

        newpairs = {}
        for key in pairs:
            char = table[key]
            first = key[0] + char
            second = char + key[1]
            newpairs[first] = newpairs.get(first,0) + pairs[key]
            newpairs[second] = newpairs.get(second,0) + pairs[key]

        pairs = newpairs
        
    return pairs

def findDifference(n: int):
    polymer, table = getData()
    newpoly = insertions(polymer, table, n)

    counts = {}
    for key in newpoly:
        num = newpoly[key]
        counts[key[0]] = counts.get(key[0], 0) + num
    
    counts[polymer[-1]] = counts.get(polymer[-1], 0) + 1

    most = None
    least = None

    for key in counts:
        val = counts[key]
        if most is None or val > most:
            most = val
        if least is None or val < least:
            least = val
        
    print("After iterating {} times on {} results in difference of {}.".format(n, polymer, most - least))


findDifference(10)
findDifference(40)

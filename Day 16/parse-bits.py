from typing import List
from typing import Tuple

filename = "input.txt"

def getData() -> List[str]:

    inp = open(filename, "r")

    data = []
    for line in inp:
        data.append(line.strip())

    inp.close()
    return data

class Packet:
    
    def __init__(self):
        self.children = []
        self.v = 0
        self.t = 0
        self.i = 0
        self.lit = 0

def parseLiteral(pack: Packet, data: str) -> int:
    lit = ""
    read = 0
    notZero = True
    while notZero:

        if data[read] == "0":
            notZero = False
        read += 1

        lit = lit + data[read:read+4]
        read += 4

    pack.lit = int(lit, 2)
    return read

def parseOperator(pack: Packet, data: str) -> int:

    pack.i = int(data[0],2)
    read = 1
    if pack.i == 0:
        pack.lit = int(data[read:read+15],2)
        read += 15
        end = read + pack.lit
        while read < end:
            child, bits = parsePacket(data[read:])
            pack.children.append(child)
            read += bits

    else:
        pack.lit = int(data[read:read+11],2)
        read += 11
        for i in range(pack.lit):
            child, bits = parsePacket(data[read:])
            pack.children.append(child)
            read += bits

    return read

def parsePacket(data: str) -> Tuple[Packet, int]:

    pack = Packet()
    pack.v = int(data[:3], 2)
    pack.t = int(data[3:6], 2)
    read = 6
    if pack.t == 4:
        read += parseLiteral(pack, data[read:])
    else:
        read += parseOperator(pack, data[read:])

    return pack, read

def hexToBinaryString(hex: str) -> str:
    binary = ""
    for char in hex:
        binary = binary + bin(int(char, 16))[2:].rjust(4, "0")   
    return binary

def sumVersions(pack: Packet) -> int:

    verTotal = pack.v
    for child in pack.children:
        verTotal += sumVersions(child)
    return verTotal

def evaluatePacket(pack: Packet) -> int:

    t = pack.t
    if t == 4:
        return pack.lit
    
    children = pack.children
    vals = []
    for child in children:
        vals.append(evaluatePacket(child))

    if t == 0:
        return sum(vals)
    if t == 1:
        product = 1
        for val in vals:
            product *= val
        return product
    if t == 2:
        return min(vals)
    if t == 3:
        return max(vals)
    if t == 5:
        return 1 if vals[0] > vals[1] else 0
    if t == 6:
        return 1 if vals[0] < vals[1] else 0
    if t == 7:
        return 1 if vals[0] == vals[1] else 0
        

def printPackets(pack: Packet, depth: int) -> None:

    print("{}v={} t={} i={} lit={}".format("\t"*depth, pack.v, pack.t, pack.i, pack.lit))
    for child in pack.children:
        printPackets(child, depth+1)

data = getData()
for hex in data:
    binary = hexToBinaryString(hex)
    packet, read = parsePacket(binary)
    printPackets(packet, 0)
    print("The version sum is {}.".format(sumVersions(packet)))
    print("This packet evaluates to {}.".format(evaluatePacket(packet)))
from typing import List

def getBits() -> int:

    inp = open("input.txt", "r")

    data = inp.readline().strip()
    inp.close()

    return len(data)

def getData() -> List[int]:

    inp = open("input.txt", "r")

    data = []
    for line in inp:
        val = int(line.strip(), 2)
        data.append(val)
    inp.close()

    return data

def powerConsumption(data: List[int], bits: int) -> int:

    gamma = 0
    epsilon = 0
    onesCount = [0] * bits

    for val in data:
        for bit in range(1, bits+1):
            onesCount[bit-1] += 1 if val >> (bits - bit) & 1 else 0

    for bit in range(1, bits+1):
        val = (1 << (bits - bit))
        gamma += val if onesCount[bit-1] >= len(data) // 2 else 0
        epsilon += val if onesCount[bit-1] < len(data) // 2 else 0

    return gamma * epsilon

def lifeSupport(data: List[int], bits: int, isOxy: bool) -> int:

    for bit in range(1, bits+1):
    
        if len(data) < 2:
            break

        zeroes = []
        ones = []

        for line in data:

            if line >> (bits - bit) & 1:
                ones.append(line)
            else:
                zeroes.append(line)

        if len(zeroes) <= len(ones):
            data = ones if isOxy else zeroes
        else:
            data = zeroes if isOxy else ones

    return data[0]

data = getData()
bits = getBits()
print(powerConsumption(data, bits))
print(lifeSupport(data, bits, True) * lifeSupport(data, bits, False))
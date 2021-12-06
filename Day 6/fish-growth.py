from typing import List

def getData():

    inp = open("input.txt", "r")

    data = inp.readline().strip().split(",")

    for i in range(0, len(data)):
        data[i] = int(data[i])

    return data

def growFish(data: List[int], days: int) -> int:

    buckets = [0] * 9

    # Initialize fish

    for num in data:
        buckets[num] += 1

    for day in range(0, days):

        zero = buckets[0]

        for i in range(1, len(buckets)):
            buckets[i-1] = buckets[i]

        buckets[6] += zero
        buckets[8] = zero

    total = 0

    for i in range(0, len(buckets)):
        total += buckets[i]

    return total

data = getData()
print(growFish(data, 256))
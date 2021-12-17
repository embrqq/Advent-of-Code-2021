from typing import List

filename = "input.txt"

def getData() -> List[List[int]]:

	inp = open(filename, "r")

	data = inp.readline().strip().strip("target area: ")
	data = data.split(", ")
	data[0] = data[0].strip("x=").split("..")
	data[1] = data[1].strip("y=").split("..")

	val1 = int(data[0][0])
	val2 = int(data[0][1])

	xmin = min(val1, val2)
	xmax = max(val1, val2)

	val1 = int(data[1][0])
	val2 = int(data[1][1])

	ymin = min(val1, val2)
	ymax = max(val1, val2)

	inp.close()

	return [[xmin, ymin], [xmax, ymax]]

def stepX(xvel: int, steps: int):

	sum1 = (xvel * (xvel+1)) // 2
	sum2 = ((xvel-steps) * ((xvel-steps)+1)) // 2

	if steps >= xvel:
		return sum1
	else:
		return sum1 - sum2


def findVelocities(coords: List[List[int]]) -> int:
	xmin = coords[0][0]
	xmax = coords[1][0]
	ymin = coords[0][1]
	ymax = coords[1][1]

	matches = 0

	for xvel in range(0, xmax+1):
		for yvel in range(0, abs(ymin)+1):
			steps = 0
			ypos = 0

			while ypos >= ymin:
				ypos += yvel - steps
				xpos = stepX(xvel, steps+1)
				if xpos >= xmin and xpos <= xmax:
					if ypos >= ymin and ypos <= ymax:
						matches += 1
						break

				steps = steps+1

			steps = 0
			ypos = 0
			while ypos >= ymin and yvel > 0:
				ypos += -yvel - steps
				xpos = stepX(xvel, steps+1)
				if xpos >= xmin and xpos <= xmax:
					if ypos >= ymin and ypos <= ymax:
						matches += 1
						break

				steps = steps+1
	
	return matches

def calculateMaxY(coords: List[List[int]]) -> int:

	ymin = coords[0][1]
	maxY = -(ymin+1)
	return (maxY * (maxY + 1)) // 2


coords = getData()
yvel = calculateMaxY(coords)
print(coords)
print("Maximum Y position is {}.".format(yvel))
print("There are {} possible starting velocities.".format(findVelocities(coords)))
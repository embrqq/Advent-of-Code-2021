from typing import List
from typing import Tuple
import math

filename = "input.txt"

class Number:

	def __init__(self, isVal: bool):
		self.isVal = isVal
		self.val = None
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):

		if self.isVal:
			return("{}".format(self.val))
		else:
			return("[{},{}]".format(self.left, self.right))

def getData() -> List[str]:

	inp = open(filename, "r")

	data = []

	for line in inp:
		data.append(line.strip())

	inp.close()
	return data

def buildNumber(data: str) -> Tuple[Number, int]:

	node = Number(False)

	# Consume opening bracket
	read = 1

	child = None
	# Build a sub tree in the left
	if data[read] == "[":
		child, chars = buildNumber(data[read:])
		read += chars
	
	# Left child is a literal
	else:
		child = Number(True)
		val = ""
		while not (data[read] == ","):
			val = val + data[read]
			read += 1
		child.val = int(val)
	
	child.parent = node
	node.left = child

	# Consume ","
	read += 1

	# Build a sub tree in the right
	if data[read] == "[":
		child, chars = buildNumber(data[read:])
		read += chars

	# Right child is a literal
	else:
		child = Number(True)
		val = ""
		while not (data[read] == "]"):
			val = val + data[read]
			read += 1
		child.val = int(val)

	child.parent = node	
	node.right = child

	# Consume "]"
	read += 1

	return node, read

def add(left: Number, right: Number) -> Number:

	root = Number(False)

	left.parent = root
	root.left = left

	right.parent = root
	root.right = right

	return root

def explode(node: Number, depth: int) -> bool:
	
	if node is None or node.isVal:
		return False

	if depth < 4:
		if explode(node.left, depth+1):
			return True
		if explode(node.right, depth+1):
			return True
		return False

	# Depth is > 4, need to explode
	
	# Find closest left number
	target = node.parent
	previous = node

	while target is not None:
		if target.left == previous:
			previous = target
			target = target.parent
		else:
			break

	# Found a branch to go down
	if target is not None:
		target = target.left
		while not target.isVal:
			target = target.right

		target.val += node.left.val


	# Find closest right number
	target = node.parent
	previous = node

	while target is not None:
		if target.right == previous:
			previous = target
			target = target.parent
		else:
			break

	# Found a branch to go down
	if target is not None:
		target = target.right
		while not target.isVal:
			target = target.left

		target.val += node.right.val

	zero = Number(True)
	zero.val = 0
	zero.parent = node.parent

	if node.parent.left == node:
		node.parent.left = zero
	else:
		node.parent.right = zero
	
	return True

def split(node: Number) -> bool:

	if not node.isVal:
		if split(node.left):
			return True
		if split(node.right):
			return True
		return False

	elif node.val >= 10:

		pair = Number(False)
		pair.parent = node.parent

		left = Number(True)
		left.val = math.floor(node.val/2)
		left.parent = pair
		pair.left = left

		right = Number(True)
		right.val = math.ceil(node.val/2)
		right.parent = pair
		pair.right = right
		
		if node.parent.left == node:
			node.parent.left = pair
		else:
			node.parent.right = pair
		
		return True


	return False

def reduce(node: Number) -> Number:

	exploded = True
	splited = True
	while exploded or splited:
		exploded = explode(node, 0)
		if exploded:
			continue
		splited = split(node)
		
	return node

def magnitude(node: Number) -> int:
	if node.isVal:
		return node.val
	
	left = magnitude(node.left)
	right = magnitude(node.right)
	return (3*left) + (2*right)


def problem1():
	data = getData()
	left = buildNumber(data[0])[0]
	for line in data[1:]:
		right = buildNumber(line)[0]
		print("Adding {} with {}.".format(left, right))

		root = add(left, right)
		print("After addition: {}.".format(root))
		reduce(root)
		left = root

	print("The final magnitude is {}.".format(magnitude(left)))

def problem2():
	data = getData()

	maxMag = 0
	for i in range(len(data)):
		for j in range(len(data)):

			if i == j:
				continue

			left = buildNumber(data[i])[0]
			right = buildNumber(data[j])[0]
			maxMag = max(maxMag, magnitude(reduce(add(left, right))))

	print("The maximum magnitued of two numbers is {}.".format(maxMag))

problem2()
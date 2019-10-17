import sys

class Collection:
	def push(self, v):
		pass
	def pop(self):
		pass

class Stack(Collection):
	def __init__(self):
		self.values = []

	def push(self, v):
		self.values.append(v)

	def pop(self):
		if self.values == []:
			return None
		else:
			return self.values.pop()

def general_search(
		g,
		origin,
		predicate,
		collection):

	visited = []
	prevs = {}
	while not predicate(origin):
		visited.append(origin)
		neighbours = [n for n in g[origin] if n not in visited]
		for n in neighbours:
			collection.push(n)
			prevs[n] = origin
		origin = collection.pop()
		if origin is None:
			return None

	path = [origin]
	actual = origin
	while actual in prevs:
		actual = prevs[actual]
		path.append(actual)
	return list(path.__reversed__())


def makeGraph(matrix):
	return {}


std = sys.stdin

T = std.readline().replace("\n", "")

for _ in range(int(T)):
	std.readline()
	matrix = []
	matrix.append(std.readline().replace("\n", ''))
	matrix.append(std.readline().replace("\n", ''))
	matrix.append(std.readline().replace("\n", ''))
	matrix.append(std.readline().replace("\n", ''))
	matrix.append(std.readline().replace("\n", ''))
	g = makeGraph(matrix)
	a = general_search(g, (0,4), (lambda x: x == (4,0)), Stack())
	if a is None:
		print("ROBBERS")
	else:
		print(a)
		print(10*'#')
		print()


from typing import List, Dict, Callable, Optional, TypeVar

Graph = Dict[int, List[int]]

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

class Queue(Collection):
	def __init__(self):
		self.values = []

	def push(self, v):
		self.values.append(v)

	def pop(self):
		if self.values == []:
			return None
		else:
			return self.values.pop(0)

def general_search(
		g: Graph,
		origin: int,
		predicate: Callable[[int], bool],
		collection: Collection) -> Optional[List[int]]:

	visited: List[int] = []
	prevs: Dict[int, int] = {}
	while not predicate(origin):
		visited.append(origin)
		try:
			neighbours = [n for n in g[origin] if n not in visited]
		except KeyError:
			return None
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

T = TypeVar('T')

def depth_first_search(
		g: Graph,
		origin: int,
		target: int,
		):
	return general_search(g, origin, (lambda x: x == target), Stack())


def hillclimbing(
		inititial_value: T,
		scoring_function: Callable[[T], float],
		neighbourhood_function: Callable[[T], List[T]],
		leq: Callable[[T, T], bool]
		) -> T:
	while True:
		neighbours = neighbourhood_function(inititial_value)
		values = [(n, scoring_function(n)) for n in neighbours]
		next_value = max(values, key=lambda x: x[1])
		if leq(next_value[0], inititial_value):
			return inititial_value
		inititial_value = next_value[0]

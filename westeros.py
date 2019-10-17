from sys import stdin
from graphs import Graph
from typing import List, Tuple, Dict, Set

N = int(stdin.readline().replace("\n", ""))

g: Graph = {}
f: Graph = {}

class Break(Exception):
	pass


try:
	for i in range(1, N+1):
		line = stdin.readline().replace("\n", "")
		g[i] = []
		for j in range(N):
			if j+1 not in f:
				f[j+1] = []
			if line[j] == 'S':
				g[i].append(j+1)
				f[j+1].append(i)
		for n in g[i]:
			for j in f[i]:
				if n not in g[j]:
					raise Break()
except Break:
	print(-1)
else:
	houses: List[List[int]] = []
	for l in g.values():
		if l not in houses:
			houses.append(l)
	houses = sorted(houses)
	print(len(houses))
	for h in houses:
		print(len(h), end=' ')
	print()

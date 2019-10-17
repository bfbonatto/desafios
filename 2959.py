import sys
from graphs import Graph, depth_first_search

STD = sys.stdin

n, m, p = STD.readline().replace("\n", "").split()
N, M, P = int(n), int(m), int(p)

g: Graph = {}

for _ in range(M):
	a, b = STD.readline().replace("\n", "").split()
	A, B = int(a), int(b)
	if A not in g:
		g[A] = [B]
	else:
		g[A].append(B)
	if B not in g:
		g[B] = [A]
	else:
		g[B].append(A)


for _ in range(P):
	k, l = STD.readline().replace("\n", "").split()
	K, L = int(k), int(l)
	path = depth_first_search(g, K, L)
	if path is None:
		print("Deu ruim")
	else:
		print("Lets que lets")

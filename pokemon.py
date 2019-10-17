import sys

stdin = sys.stdin

while True:
	nk = stdin.readline().replace("\n", "")
	if nk == "":
		break
	n, k = nk.split()
	N = int(n)
	W = int(k)

	candies = stdin.readline().replace("\n", "").split()

	v = sorted([int(v) for v in candies])

	weights = stdin.readline().replace("\n", "").split()

	w = sorted([int(v) for v in weights])

	m = {}

	for j in range(W+1):
		m[(-1,j)] = 0

	for i in range(N):
		for j in range(W):
			if w[i] > j:
				m[(i,j)] = m[(i-1,j)]
			else:
				m[(i,j)] = max(m[(i-1, j)], m[(i-1, j-w[i])] + v[i])


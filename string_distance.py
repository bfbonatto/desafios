import sys


def dist(s, t):
	d = {(i,j): 0 for i in range(len(s)) for j in range(len(t))}
	for i in range(len(s)):
		d[(i, -1)] = i
	for j in range(len(t)):
		d[(-1, j)] = j

	d[(-1, -1)] = 0

	for j in range(len(t)):
		for i in range(len(s)):
			substitutionCost = 0
			if s[i] != t[j]:
				substitutionCost = 1

			d[(i,j)] = min(d[(i-1, j)] + 1, d[(i, j-1)] + 1, d[(i-1, j-1)] + substitutionCost)

	return d[(len(s)-1, len(t)-1)]


STDIN = sys.stdin

source = STDIN.readline().replace("\n", "")
k = int(STDIN.readline().replace("\n", ""))

m = 101
index = 0
mi = 0
for s in STDIN.readlines():
	s = s.replace("\n", "")
	if s == "":
		continue
	d = dist(source, s)
	index += 1
	if d < m:
		m = d
		mi = index

if m < k:
	print(mi)
	print(m)
else:
	print(-1)

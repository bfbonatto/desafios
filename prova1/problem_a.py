import sys

n = int(sys.stdin.readline().replace("\n", ""))

for i in range(n):
	[a, b, c] = sys.stdin.readline().replace("\n","").split()
	l = sorted([int(a), int(b), int(c)])
	print("Case {0}: {1}".format(str(i+1), str(l[1])))



from itertools import combinations
import sys

STD = sys.stdin

for line in STD:
	[_, sk] = line.replace("\n", '').split()
	k = int(sk)
	l = [int(v) for v in STD.readline().replace("\n", '').split()]
	average = sum(sorted(combinations(l,3), key=(lambda x: (x[0] + x[1] + x[2])/3), reverse=True)[k-1])
	print("{:0.1f}".format(average/3))


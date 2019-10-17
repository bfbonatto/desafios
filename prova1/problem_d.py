import sys

stdin = sys.stdin

n = int(stdin.readline().replace("\n", ""))
evens = []
odds = []
for _ in range(n):
	i = int(stdin.readline().replace("\n", ""))
	if i % 2 == 0:
		evens.append(i)
	else:
		odds.append(i)

evens = sorted(evens)
odds = sorted(odds, reverse=True)
for e in evens:
	print(e)
for o in odds:
	print(o)

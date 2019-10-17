import sys

stdin = sys.stdin

def other(foot):
	if foot == "E":
		return "D"
	else:
		return "E"


while True:
	s = stdin.readline()
	if s == "":
		break
	n = int(s.replace("\n", ""))
	boots = {(m, f): 0 for m in range(30, 61) for f in ["E", "D"]}
	n_pairs = 0
	for _ in range(n):
		[s_string, foot] = stdin.readline().replace("\n", "").split()
		size = int(s_string)
		if boots[(size, other(foot))] > 0:
			boots[(size, other(foot))] -= 1
			n_pairs += 1
		else:
			boots[(size, foot)] += 1
	print(n_pairs)



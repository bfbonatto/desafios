from sys import stdin


def components(tree, p, current=[]):
	if p not in current:
		current.append(p)
		for n in tree[p]:
			current += components(tree, n, current)
		return current
	return []

lines = stdin.readlines()

trees = {}

for l in lines[1:]:
	p1, _, p2 = l.replace("\n", "").split()
	if p1 not in trees:
		trees[p1] = []
	trees[p1].append(p2)
	if p2 not in trees:
		trees[p2] = []
	trees[p2].append(p1)

n_components = 0
visited = []
for pessoa in trees.keys():
	if pessoa not in visited:
		n_components += 1
		visited += components(trees, pessoa)

print(n_components)

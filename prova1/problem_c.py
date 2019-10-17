import sys

stdin = sys.stdin

while True:
	n = int(stdin.readline().replace("\n", ""))
	if n == 0:
		break
	posts = [int(p) for p in stdin.readline().replace("\n", "").split()]
	new_posts = [e for e in posts]
	if posts[-1] == 0:
		for i in range(len(posts)):
			new_posts[i] = posts[i-1]
		posts = new_posts
	replacements = 0
	for i in range(n-1):
		a = posts[i]
		b = posts[i+1]
		if a == b and a == 0:
			posts[i+1] = 1
			replacements += 1
	if posts[-1] == posts[0] and posts[-1] == 0:
		replacements += 1
	print(replacements)


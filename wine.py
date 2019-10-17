
import sys


STD = sys.stdin

n = STD.readline().replace("\n", '')
while n != "0":
	wines = [int(w) for w in STD.readline().replace("\n", '').split()]
	work = 0
	for i in range(len(wines)-1):
		wines[i+1] += wines[i]
		work += abs(wines[i])
	print(work)



	n = STD.readline().replace("\n",'')

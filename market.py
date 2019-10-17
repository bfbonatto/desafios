import sys

try:
	cases = int(input().replace("\n", ''))

	for _ in range(cases):
		number_of_prices = int(input().replace("\n", ''))
		prices = {}
		for _ in range(number_of_prices):
			[name, value] = input().replace("\n", '').split()
			prices[name] = float(value)
		size_of_list = int(input().replace("\n", ''))
		shopping_list = {}
		for _ in range(size_of_list):
			[name, number] = input().replace("\n", '').split()
			shopping_list[name] = int(number)

		price = 0.0
		for (k, v) in shopping_list.items():
			price += v * prices[k]
		print("R$ {:0.2f}".format(price))

except:
	pass

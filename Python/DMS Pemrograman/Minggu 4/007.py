import random

seed = int(input())
random.seed(seed)

list_bilangan = random.sample(range(1, 100), 20)

for x in list_bilangan:
	if x%2 == 1:
		print (x, end=" ")

print ()
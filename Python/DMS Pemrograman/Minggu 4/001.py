import random

tanggal = input()

random.seed(tanggal)

hujan = random.choice([True, False])
panas = random.choice([True, False])

if not hujan and not panas :
	print ("Yeay, kalian bisa pergi bermain!")
else :
	print ("Wah, cuacanya tidak mendukung! Lain waktu saja ya :(")
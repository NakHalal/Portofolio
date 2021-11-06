nilai = list(map(int, input("").split(" ")))

jumlah = 0

for x in nilai:
	jumlah += x

print ( "{:.2f}".format(jumlah/len(nilai)))
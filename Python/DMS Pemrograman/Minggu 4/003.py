siswa = input("Masukkan nama siswa: ").split(" ")

for x in siswa:
	print ("Masukkan nilai", x,": ", end="")
	nilai = int(input())
	while nilai < 75:
		print ("Remedial, masukkan nilai", x,": ", end = "")
		nilai = int(input())
	print()
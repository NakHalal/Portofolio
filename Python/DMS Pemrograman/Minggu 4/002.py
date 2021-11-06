kelakuan_buruk = (input("Apakah anda memiliki riwayat berkelakuan buruk? ") == "YA")
prestasi = (input("Apakah anda memiliki prestasi akademik/non-akademik? ") == "YA")
nilai1, nilai2, nilai3 = map(int, input("Masukkan 3 nilai anda (dipisahkan dengan spasi): ").split(" "))

rata2 = (nilai1 + nilai2 + nilai3)/3

if ((not kelakuan_buruk or prestasi) and rata2 > 80) :
	print ("Selamat, anda siswa terpuji!")
else :
	print ("Maaf, berusahalah lebih giat lagi")
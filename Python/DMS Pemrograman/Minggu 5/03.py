"""3
Buatlah program untuk menentukan seragam yang harus digunakan Budi setiap harinya.
- minta inputan hari dari user
- minta inputan tanggal dari user
- minta inputan apakah tanggal tersebut tanggal merah atau tidak (Ya/Tidak)

Berikut adalah ketentuan seragamnya dengan prioritas aturan tertinggi ke terendah.
- hari libur pasti seragamnya adalah "Bebas"
- hari jum"at seragamnya adalah "Olah Raga", tetapi kalau hari jum"at bertepatan 
dengan tanggal 1 (awal bulan) maka seragamnya adalah "Batik"
- hari lainnya berseragam "Putih"

CONTOH:
Masukkan hari: Jum'at
Masukkan tanggal: 1
Tanggal Merah (Ya/Tidak): Tidak
Batik"""

hari = input("Masukkan hari:")
tgl = int(input("Masukkan tanggal:"))
merah = input("Tanggal Merah (Ya/Tidak):")

if hari == "Sabtu" or hari == "Minggu" or merah == "Ya":
    print ("Bebas")
elif hari == "Jum\'at" and merah == "Tidak": 
    if tgl == 1:
        print("Batik")
    else:
        print ("Olahraga")
elif hari == "Senin" or hari == "Selasa" or hari == "Rabu" or hari == "Kamis" and merah == "Tidak":
    print("Putih")
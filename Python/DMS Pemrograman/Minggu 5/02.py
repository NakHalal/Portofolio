"""2
Buatlah program untuk mengubah nama hari menjadi angka:
- Senin --> 1
- Selasa --> 2
- Rabu --> 3
- Kamis --> 4
- Jum'at --> 5
- Sabtu --> 6
- Minggu --> 7

Selain nama hari di atas, outputkan "Tidak Valid"

CONTOH:
Masukkan hari: Selasa
2"""

hari = input("Masukkan hari:")

if hari == "Senin" or hari == "senin":
    print("1")
elif hari == "Selasa" or hari == "selasa":
    print("2")
elif hari == "Rabu" or hari == "rabu":
    print("3")
elif hari == "Kamis" or hari == "kamis":
    print("4")
elif hari == "Jum\'at" or hari == "jum\'at":
    print("5")
elif hari == "Sabtu" or hari == "sabtu":
    print("6")
elif hari == "Minggu" or hari == "minggu":
    print("7")
else:
    print("Tidak Valid")
"""6
Buatlah program yang meminta user menginputkan sebuah nilai integer positif n.
Lalu outputkan semua angka ganjil dari 1 sampai n.

CONTOH:
Masukkan batas akhir: 12
1
3
5
7
9
11"""

nilai = int(input("Masukkan batas akhir: "))

for i in range(1, nilai+1, 2):
    print (i)
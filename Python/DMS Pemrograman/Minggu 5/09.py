"""9
Buatlah program untuk menjumlah semua angka yang diinputkan satu per satu oleh user.

Minta user untuk menginput banyaknya nilai yang ingin dijumlahkan.
Minta user menginputkan satu per satu nilainya
Print hasil penjumlahan

CONTOH:
Banyaknya nilai: 5
Masukkan nilai ke-1: 10
Masukkan nilai ke-2: -20
Masukkan nilai ke-3: 20
Masukkan nilai ke-4: 30
Masukkan nilai ke-5: 15
55"""

x=int(input("Masukan jumlah perulangan : "))

jml = 0
for i in range (1,x+1):
    print("\nMasukan nilai ke-",i) 
    nilai = int(input())
    jml=jml+nilai
    print ("\nJumlah saat ini adalah :",jml)
print("Hasil penjumlahan adalah :",jml)
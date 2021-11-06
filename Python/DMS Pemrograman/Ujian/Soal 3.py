"""
Buatlah sebuah program yang akan terus menerima inputan berupa integer sampai total
penjumlahan angka yang diinputkan lebih dari 500. Output dari program berupa total penjumlahan
angka yang diinputkan, rata-rata dan banyak angka yang diinputkan.
"""

total=0
n=0
while total <=500:
    tambah = int(input("Inputkan angka: "))
    total = total + tambah
    n = n + 1
print("Total angka yang diinputkan:",total)
print("Rata-rata angka yang diinputkan:",total/n)
print("Banyak angka yang diinputkan:",n)


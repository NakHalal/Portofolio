"""7	Minta user menginputkan sebuah bilangan integer positif n.
Lalu outputkan pola '*' n x n.

CONTOH:
Masukkan n: 5
*****
*****
*****
*****
*****
"""

n = int(input("Masukan angka : " ))
for i in range(0, n):
    for j in range(0, n):
        print('*', end='')
    print()





"""nilai = int(input("Masukan angka : "))
if nilai > 0:
    for i in range (0, nilai):
        print(nilai*("*"))
else:
    print("Input Tidak Valid!")"""
"""10
Buat program meminta inputan integer positif n dari user. 
Selama yang diinputkan <=0, program terus minta user menginputkan lagi.

Jika inputan sudah valid, outputkan bintang sebanyak n kali.

CONTOH:
Masukkan integer > 0: 0
Input Tidak Valid!
Masukkan integer > 0: -1
Input Tidak Valid!
Masukkan integer > 0: 5
*****
"""

while True:
    nilai = int(input("Masukan integer > 0: "))
    if nilai > 0:
        print("*"*nilai)
    else:
        print("Input Tidak Valid!")
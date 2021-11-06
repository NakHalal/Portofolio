"""10	Buat program meminta inputan integer positif n dari user. 
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



"""while True:
    bil=input("Masukan angka disini! \n")
    try:
        bil=int(bil)
        if bil%2==0:
            print("Genap\n")
        else:
            print("Ganjil\n")
    except:
        if bil=="selesai":
            break
        else:
            print("Masukan angka yang valid!\n")
print("Terima Kasih")"""

"""11
Buat program meminta inputan integer positif n dari user. 
Selama yang diinputkan <=0, program terus minta user menginputkan lagi 
sampai MAKSIMAL 3 kali.

Jika n valid, outputkan bintang sebanyak n kali. 
Jika n masih tidak valid, tidak menampilkan apapun.

CONTOH:
Masukkan integer > 0: -1
Input Tidak Valid!
Anda punya maksimal 3 percobaan lagi:
Masukkan integer > 0: -2
Input Tidak Valid!
Anda punya maksimal 2 percobaan lagi:
Masukkan integer > 0: -5
Input Tidak Valid!
Anda punya maksimal 1 percobaan lagi:
Masukkan integer > 0: 0"""

batas = 3
while True:
    nilai = int(input("Masukan integer > 0: "))
    
    if nilai > 0 and batas > 0:
        print("*"*nilai)
    else:
        if batas==0:
            print("Batas anda telah habis!")
            break
        else:
            print("Input Tidak Valid!")
            print("Anda punya maksimal",batas,"percobaan lagi: ")
            batas=batas-1
        
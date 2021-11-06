"""4
Buatlah program untuk menghitung total diskon yang diterima oleh pembeli.
- meminta inputan total belanja dari user
- meminta inputan apakah member atau bukan

Berikut aturan diskon yang bisa diakumulasikan.
- diskon member adalah 5%
- pembelian 500.000 - 1 juta dapat diskon 2%, 
sedangkan pembelian di atas 1 juta dapat diskon 3%

Outputkan total diskon dalam persen.

CONTOH:
Masukkan total belanja: 600000
Apakah member (Ya/Tidak): Ya 
Anda mendapat diskon 7%"""

belanja = int(input("Masukkan total belanja :"))
member = input("Apakah member? (Ya/Tidak) :")

if belanja > 500000 and belanja < 1000000:
    if member == "Ya":
        print ("Anda mendapatkan diskon 7%")
    elif member == "Tidak":
        print ("Anda mendapatkan diskon 2%")
elif belanja > 1000000:
    if member == "Ya":
        print ("Anda mendapatkan diskon 8%")
    elif member == "Tidak":
        print ("Anda mendapatkan diskon 3%")
elif belanja < 500000:
    if member == "Ya":
        print ("Anda mendapatkan diskon 5%")
    elif member == "Tidak":
        print ("Anda tidak mendapatkan diskon")

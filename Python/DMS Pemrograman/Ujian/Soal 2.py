"""
Buatlah sebuah program yang akan menerima input berupa empat jawaban pertanyaan berikut:
- apakah punya voucher promo? (ya/tidak)
- total belanja?
- apakah punya kartu anggota? (ya/tidak)
- tanggal hari ini?
kemudian program akan menge-outputkan besaran diskon dengan ketentuan sebagai berikut:
(1) Seorang member PASTI akan mendapatkan diskon sebesar 5%
(2) Jika mempunyai voucher promo, mendapat diskon tambahan (besarnya sesuai dengan tanggal),
HANYA untuk total belanja &gt; 100000 (seratus ribu)
(3) HANYA JIKA syarat nomor (2) terpenuhi. Diskon tambahan dari voucher promo sebesar 10% akan
diberikan untuk pembeli yang MEMPUNYAI VOUCHER PROMO dan belanja di tanggal 11-20.
Pembelian di tanggal 1-10 atau 21-31 bagi pembeli yang MEMPUNYAI VOUCHER PROMO akan diberi
diskon tambahan 5%.
"""

print("apakah punya voucher promo? (ya/tidak)")
print("total belanja?")
print("apakah punya kartu anggota? (ya/tidak)")
print("tanggal hari ini?")

promo = input()
total = int(input())
kartu = input()
tanggal = int(input())

diskon = 0
if kartu == ("ya"):
    diskon = diskon + 5
if promo == ("ya") and total >100000:
    if tanggal >= 11 and tanggal <= 20:
        diskon = diskon + 10
    elif(tanggal >= 1 and tanggal <=10) or (tanggal >= 21 and tanggal <=31):
        diskon = diskon + 5
print("diskon",diskon,"%")

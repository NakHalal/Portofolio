A = int(input("Masukkan Besar Voucher Diskon (50000, 100000, atau 150000) yang Anda Punya: "))
B = input("Sudah Pernah Berbelanja Disini? (Ya/Belum): ")
C = input("Apakah Anda Memiliki Kartu Anggota? (Ya/Tidak): ")
D = int(input("Total Belanja: "))

B = B.lower()
C = C.lower()

Diskon = 0

if B == 'belum':
    Diskon += 50000
if B == 'ya' and (A == 50000 or A == 100000 or A == 150000):
    Diskon += A
if C == 'ya' and D > 500000:
    Diskon += 50000
    
print('Total Potongan Harga:', Diskon)
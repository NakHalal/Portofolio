jumlahtahun = int(input("Masukan tahun: "))
Baris = 0
MahasiswaAktifLama = 0

while jumlahtahun != 0:
    mi, mo, ma = map(int, input("Masukan Data: ").split())
    MahasiswaAktifLama = MahasiswaAktifLama + mi - mo
    if MahasiswaAktifLama == ma:
        Baris = Baris + 1
    jumlahtahun = jumlahtahun - 1

print(Baris + 1)
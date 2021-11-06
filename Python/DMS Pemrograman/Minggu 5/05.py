"""5
Buatlah program untuk menghitung gaji pegawai.
Minta input status pegawai.
Jika pegawai berstatus "Tetap", maka minta input jumlah anak.
Gaji pegawai "Tetap" adalah:
- gaji pokok 6 juta
- tunjangan anak yaitu 220000/anak jika jumlah anak <= 3. Jika > 3, maka 200000/anak

Gaji pegawai "Kontrak" yaitu 4000000

CONTOH:
Masukkan status pegawai (Tetap/Kontrak): Tetap
Masukkan jumlah anak: 5
Gaji anda adalah 7000000"""

status = input("Masukkan status pegawai (Tetap/Kontrak) :")

if status == "Tetap":
    anak = int(input("Masukkan jumlah anak: "))
    if anak <= 3:
        gaji = 6000000 + (anak*220000)
        print("Gaji anda adalah", gaji)
    elif anak > 3:
        gaji2 = 6000000 + (anak*200000)
        print("Gaji anda adalah", gaji2)
elif status == "Kontrak":
    print ("Gaji anda adalah 4000000")

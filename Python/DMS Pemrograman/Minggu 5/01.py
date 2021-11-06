"""1
Buatlah program untuk memeriksa apakah inputan user 
merupakan nama hari yang valid atau tidak.
Nama hari yang valid adalah: 
- Senin
- Selasa
- Rabu
- Kamis
- Jum'at
- Sabtu
- Minggu"""


hari = input()
if hari == "Senin" or hari == "Selasa" or hari == "Rabu" or hari == "Kamis" or hari == "Jum'at" or hari == "Sabtu" or hari == "Minggu":
    print("valid")
else:
    print("tidak valid")
"""
Buatlah sebuah fungsi untuk menentukan apakah nilai di parameter fungsi merupakan bilangan
kelipatan 3 dan kelipatan 5. Fungsi akan mengembalikan nilai True jika terpenuhi dan False jika
tidak terpenuhi. Proses meminta input dari user dan mengoutputkan ke layar dilakukan di
program utama.
"""

n = int(input("Masukkan nilai: "))

if n % 3 == 0 and n % 5 == 0:
    print("True")
else:
    print("False")
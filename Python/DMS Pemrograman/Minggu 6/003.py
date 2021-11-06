nilai_saldo = int(input())

def printMenu():
  print("1. es teh manis: 50")
  print("2. es kelapa: 100")
  print("3. es jeruk: 150")

while nilai_saldo > 0:
  printMenu()
  pesan = int(input("Masukkan angka pesanan anda: "))
  nilai_saldo -= pesan*50
  print ("Sisa saldo anda: ", nilai_saldo)
  print ()
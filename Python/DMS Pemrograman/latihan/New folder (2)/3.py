saldo = int(input())

def printMenu():
  print("1. es teh manis: 50")
  print("2. es kelapa: 100")
  print("3. es jeruk: 150")
  
#your code start here
while saldo > 0:
    printMenu()
    a = int(input('Masukkan angka pesanan anda: '))
    if a == 1:
        saldo -= 50
        print('Sisa saldo anda: ', saldo)
    elif a == 2:
        saldo -= 100
        print('Sisa saldo anda: ', saldo)
    elif a == 3:
        saldo -= 150
        print('Sisa saldo anda: ', saldo)
    print()
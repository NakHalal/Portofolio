"""
Buatlah program yang akan menerima sebuah bilangan bulat N dan mencetak pola seperti contoh.
"""
a = int(input())
for i in range(0,a):
    for j in range(0,i+1):
        print(j,"",end="")
    print("")
for i in range(0, a):
    for j in range(0,a-1):
        print(j,"",end="")
    a-=1
    print("")


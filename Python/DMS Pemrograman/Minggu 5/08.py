"""8
Minta user menginputkan sebuah bilangan integer positif n.
Lalu outputkan pola n x n, dikelilingi '*' dan di dalamnya '#'.

CONTOH:
Masukkan n: 5
*****
*###*
*###*
*###*
*****"""

n=int(input("Masukan angka : "))
for i in range(n):
    for j in range(n):
        if(i==0 or i == n-1 or j==0 or j==n-1):
            print("*", end = "")
        else:
            print("#", end = "")
    print()
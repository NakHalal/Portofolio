"""
def fact(n):
    &#39;&#39;&#39;
    Fungsi menghitung faktorial
 
    Parameter:
    n(integer): bilangan yang ingin difaktorialkan, harus berupa integer non-
negatif
    &#39;&#39;&#39;
    hasil = 1
    for i in range(1,n+1):
        hasil *= i
    return hasil
   
def
perm(n,r):
    &#39;&#39;&#39;
    Fungsi untuk menghitung n permutasi r
 
    Parameter:
    n, r (integer): harus berupa integer non-negatif, dan n harus &gt;= r.
    &#39;&#39;&#39;
    return fact(n)//fact(n-r)
 
n,r = map(int,input().split())
print(perm(n,r))
"""
def fact(n):
    hasil = 1
    for i in range (1,n+1):
        hasil = hasil*1
    return hasil
def perm(n,r):
    return fact(n)//facnt(n-r)
    n,r = map(int, input().split()
    print(perm(n,r))
    if n<0 or r<0:
        print("seharusnya tidak ada hasil, nilai n dan r harus positif")
    elif: r>n:
        print("seharusnya tidak ada hasil, karena nilai r>n")
    else:
        print("benar")
def fact(n):
    """
    Fungsi menghitung faktorial
 
    Parameter:
    n(integer): bilangan yang ingin difaktorialkan, harus berupa integer non-negatif
    """
    hasil = 1
    for i in range(1,n+1):
        hasil *= i
    return hasil

def perm(n,r):
    """
    Fungsi untuk menghitung n permutasi r
 
    Parameter:
    n, r (integer): harus berupa integer non-negatif, dan n harus >= r.
    """
    return fact(n)//fact(n-r)

n,r = map(int,input().split())
if r > n:
    print("nilai r lebih besar dari n.")
else:
    print(perm(n,r))

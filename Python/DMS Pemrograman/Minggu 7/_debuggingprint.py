#Sebelum di revisi
"""#Fungsi
def sum_genap_ganjil(n):
    
    assert isinstance(n, int) and n >= 0, "n harus berupa non-negatif integer"
    
    sum1 = 0
    sum2 = 0
    for i in range(1, n):
        if i % 2 == 1: #ganjil
            suml = sum1 + i
        else: #genap
            sum2 = sum2 + i
    return sum1, sum2""" 
#Sesudah di revisi
# sum_genap_ganjil.py

#Fungsi
def sum_genap_ganjil(n):
    
    assert isinstance(n, int) and n >= 0, "n harus berupa non-negatif integer"
    
    sum1 = 0
    sum2 = 0
    for i in range(1, n+1):
        if i % 2 == 1: #ganjil
            sum1 = sum1 + i
        else: #genap
            sum2 = sum2 + i
    return sum1, sum2
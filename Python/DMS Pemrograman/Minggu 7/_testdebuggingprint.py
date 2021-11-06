#Sebelum revisi
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
    return sum1, sum2

# MainCode

print(sum_genap_ganjil(0) == (0, 0)) # gunakan tuple () jika terdapat lebih dari 1 nilai pada return
print(sum_genap_ganjil(1) == (1, 0))
print(sum_genap_ganjil(2) == (1, 2))
print(sum_genap_ganjil(5) == (9, 6))
print(sum_genap_ganjil(6) == (9, 12))"""

#Sesudah Revisi

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

# MainCode

print(sum_genap_ganjil(0) == (0, 0)) # gunakan tuple () jika terdapat lebih dari 1 nilai pada return
print(sum_genap_ganjil(1) == (1, 0))
print(sum_genap_ganjil(2) == (1, 2))
print(sum_genap_ganjil(5) == (9, 6))
print(sum_genap_ganjil(6) == (9, 12))
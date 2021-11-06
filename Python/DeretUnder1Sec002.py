"""ID: Buatlah sebuah fungsi Python 3 sum(n) yang mengambil bilangan bulat positif 𝑛n sebagai masukan dan melakukan komputasi:

𝑠𝑢𝑚(𝑛)=1−2+3−4+⋯+(−1)𝑛+1𝑛sum(n)=1−2+3−4+⋯+(−1)n+1n.

Nilai dari 𝑛n antara 11 dan 10151015. Batas waktu komputasi adalah 11 detik. Untuk membuat kode program efisien, coba gunakan formula eksplisit (bentuk tertutup) dari 𝑠𝑢𝑚(𝑛)sum(n).

For example:

Test and Result
print(sum(1)) = 1
print(sum(2)) = -1
print(sum(3)) = 2
print(sum(4)) = -2
"""
def sum(n):
    if n % 2 == 0: return -1*(n//2)
    else: return -1*((n-1)//2)+n

print(sum(1))
print(sum(2))
print(sum(3))
print(sum(4))
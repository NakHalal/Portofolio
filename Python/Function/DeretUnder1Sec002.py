"""ID: Buatlah sebuah fungsi Python 3 sum(n) yang mengambil bilangan bulat positif ðn sebagai masukan dan melakukan komputasi:

ð ð¢ð(ð)=1â2+3â4+â¯+(â1)ð+1ðsum(n)=1â2+3â4+â¯+(â1)n+1n.

Nilai dari ðn antara 11 dan 10151015. Batas waktu komputasi adalah 11 detik. Untuk membuat kode program efisien, coba gunakan formula eksplisit (bentuk tertutup) dari ð ð¢ð(ð)sum(n).

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
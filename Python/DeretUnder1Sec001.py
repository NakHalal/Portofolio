'''
ID: Buatlah sebuah fungsi Python 3 sum(n) yang mengambil bilangan bulat positif ðn sebagai masukan dan melakukan komputasi:

ð ð¢ð(ð)=5+10+â¯+5(ðâ1)+5ðsum(n)=5+10+â¯+5(nâ1)+5n.

Nilai dari ðn antara 11 dan 10151015. Batas waktu komputasi adalah 11 detik. Untuk membuat kode program efisien, coba gunakan formula eksplisit (bentuk tertutup) dari ð ð¢ð(ð)sum(n).

For example:

Test and Result:
print(sum(1)) = 5
print(sum(2)) = 15
print(sum(3)) = 30
'''

def sum(n):
    return 5 * (n * (n + 1) // 2)
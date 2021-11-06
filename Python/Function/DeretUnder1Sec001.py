'''
ID: Buatlah sebuah fungsi Python 3 sum(n) yang mengambil bilangan bulat positif 𝑛n sebagai masukan dan melakukan komputasi:

𝑠𝑢𝑚(𝑛)=5+10+⋯+5(𝑛−1)+5𝑛sum(n)=5+10+⋯+5(n−1)+5n.

Nilai dari 𝑛n antara 11 dan 10151015. Batas waktu komputasi adalah 11 detik. Untuk membuat kode program efisien, coba gunakan formula eksplisit (bentuk tertutup) dari 𝑠𝑢𝑚(𝑛)sum(n).

For example:

Test and Result:
print(sum(1)) = 5
print(sum(2)) = 15
print(sum(3)) = 30
'''

def sum(n):
    return 5 * (n * (n + 1) // 2)
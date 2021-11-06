"""
Modifikasi kode berikut agar dapat menangani error:
 karena kesalahan input user yaitu input bukan bilangan bulat. Maka tampilkan pesan
&quot;Input bukan bilangan bulat sehingga diganti menjadi nilai default 1&quot;.
Lalu assign variable yang salah input dengan nilai 1.
 karena pembagian dengan 0. Cukup tampilkan pesan error dan program selesai tanpa
menampilkan tulisan &quot;Hasil pembagian...&quot;
bil1 = int(input(&quot;Masukkan bilangan bulat pertama: &quot;))
bil2 = int(input(&quot;Masukkan bilangan bulat kedua: &quot;))
hasil = bil1 / bil2
print(&#39;Hasil pembagian adalah&#39;, hasil)
 
Contoh hasil yang diharapkan:
Masukkan bilangan bulat pertama: 2o
Input bukan bilangan bulat, diganti menjadi nilai default 1
Masukkan bilangan bulat kedua: 5
Hasil pembagian adalah 0.2
Contoh hasil yang diharapkan:
Masukkan bilangan bulat pertama: 20
Masukkan bilangan bulat kedua: 0
division by zero
"""

bil1 = input("input bilangan bulat pertama: ")
try:
    int(bil1)
except:
    print("input bukan bilangan bulat, diganti menjadi nilai default 1")
    bil1 = 1
bil2 = input("input bilangan bulat kedua: ")
try:
    int(bil2)
except:
    print("input bukan bilangan bulat, diganti menjadi nilai default 1")
    bil2 = 1
hasil = int(bil1)/int(bil2)
print("hasil pembagian adalah",hasil)
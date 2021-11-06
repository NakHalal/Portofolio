"""
Buatlah fungsi untuk menghitung jarak dari kota A ke kota B jika diketahui kecepatan kendaraan dan waktu tempuh. Rumus jarak = kecepatan X waktu. Proses meminta input dari user dan mengoutputkan ke layar dilakukan di program utama.
"""

"""
kecepatan =  int(input("Masukan kecepatan : "))
waktu = int(input("Masukan waktu : "))

jarak = kecepatan*waktu

print(jarak)
"""

#fungsi rumus
def Rumus(k, w):
    jarak = k*w
    return jarak

#program utama
kecepatan =  int(input("Masukan kecepatan : "))
waktu = int(input("Masukan waktu : "))

j = Rumus(kecepatan,waktu)
print ("Jarak =",j)


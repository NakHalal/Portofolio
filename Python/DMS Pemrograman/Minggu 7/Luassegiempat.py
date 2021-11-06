#Fungsi
def luas_segiempat(x0, y0, x1, y1):
    """ Menghitung luas segi empat berdasarkan koordinat 2 titik: pojok kiri bawah (x0, y0), dan kanan atas (x1, y1).
    """

    # untuk memastikan koordinat input sudah sesuai asumsi
    assert x0 < x1 and y0 < y1, "koordinat tidak valid"

    deltax = x1 - x0
    deltay = y1 - y0
    return deltax * deltay

#Main Program
count = 0
while count < 3: # Memastikan bahwa akan ada 4 nilai integer yang valid
    try:
        x0 = int(input("Masukan Koordinat x0: "))
        y0 = int(input("Masukan Koordinat y0: "))
        x1 = int(input("Masukan Koordinat x1: "))
        y1 = int(input("Masukan Koordinat y1: "))
    except ValueError:
        count += 1
        print("Koordinat harus integer. Sisa percobaan:",3-count)
    else:
        luas = luas_segiempat(x0, y0, x1, y1)
        print("Luas segi empat adalah", luas)
        break
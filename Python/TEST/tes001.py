def luas_segiempat(x0, y0, x1, y1):
    """ Menghitung luas segi empat berdasarkan koordinat 2 titik: pojok kiri bawah (x0, y0), dan kanan atas (x1, y1).
    """

    # untuk memastikan koordinat input sudah sesuai asumsi
    assert x0 < x1 and y0 < y1, "koordinat tidak valid"

    deltax = x1 - x0
    deltay = y1 - y0
    return deltax * deltay
#        luas_segiempat(x0, y0, x1, y1)

x0 = 0; x1 = 0; y0 = 0; y1 = 0

def P():
    try:
        global x0, x1, y0, y1
        x0 = int(input("Koordinat x0:"))
        y0 = int(input("Koordinat y0:"))
        x1 = int(input("Koordinat x1:"))
        y1 = int(input("Koordinat y1:"))
    except:
        print("Koordinat harus integer")
        P()

P()

luas = luas_segiempat(x0, y0, x1, y1)
print("Luas segi empat adalah:", luas)

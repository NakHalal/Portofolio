#Function
def konversi_nilai(nilai):
    """menerima input berupa float 0 <= nilai <= 100 (antara 0 sampai 100)
    return "A" jika nilai > 80, "B" jika 50 < nilai <= 80, "E" selainnya.
    """

    assert 0 <= nilai and nilai <= 100, "nilai harus antara 0 sampai 100"

    if nilai > 80:
        return "A"
    elif nilai > 50:
        return "B"
    else:
        return "E"

#MainProgram
print("Test case 1:", konversi_nilai(80) == "B")
print("Test case 2:", konversi_nilai(80.01) == "A")
print("Test case 3:", konversi_nilai(50) == "E")
print("Test case 4:", konversi_nilai(50.01) == "B")
print("Test case 5:", konversi_nilai(100) == "A")
print("Test case 6:", konversi_nilai(0) == "E")
try:
    r = konversi_nilai(100.01)
    print("Test case 7: False")
except:
    print("Test case 7: True")
try:
    r = konversi_nilai(-1)
    print("Test case 8: False")
except:
    print("Test case 8: True")

print('Pengujian selesai')
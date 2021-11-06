A = 0.0
B = 0
C = 0

while C <= 125.3:
    try:
        A = float(input("Inputkan Angka: "))
        B += 1
        C += A
    except Exception:
        pass

print("Total Angka yang Diinputkan: {}".format(C))
print("Banyak Angka yang Diinputkan: {}".format(B))

x1, x2, x3 = map(int, input().split())
if x1 + x2 > x3 and x2 + x3 > x1 and x3 + x1 > x2:
    print("Segitiga")
else:
    print("Bukan Segitiga")
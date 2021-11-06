a, x, y = map(int, input().split())
if a%x==0 and a%y!=0:
    print("YA")
else:
    print("Tidak")

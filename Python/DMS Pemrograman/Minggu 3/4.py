r = int(input())
if r %7 ==0:
    PHI=22/7
    luas=PHI*r**2
else:
    PHI=3.14
    luas=PHI*r**2
print("Luas lingkaran berjari jari {} adalah {:.2f}".format(r,luas))
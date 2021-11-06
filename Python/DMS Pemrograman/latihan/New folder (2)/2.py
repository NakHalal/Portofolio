a = int(input())
b = int(input())
c = int(input())
phi = 3.14

def vol(r, t, r1):
    volume = 1/3*phi*t*(r1**2+r*r1+r**2)
    return volume

print('{:.2f}'.format(vol(a, c, b)))
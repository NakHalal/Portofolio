phi = 3.14

def volume(r, R, t):
  return phi*t*(R*R + R*r + r*r)/3

r = int(input())
R = int(input())
t = int(input())
print ("{:.2f}".format(volume(r, R, t)))
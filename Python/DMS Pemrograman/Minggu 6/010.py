pi = 3.14
def hitungVolumeSilinder(r, t):
  return r*r*pi*t

def isiAir(kapasitas, jari2, tinggiAir):
  i = 0
  for x in tinggiAir:
    volume = hitungVolumeSilinder(jari2, x)
    if kapasitas - volume > 0:
      kapasitas -= volume
      i += 1
    else :
      break
  return i

kapasitas = int(input())
jari2 = int(input())
tinggiAir = list(map(int, input().split(" ")))

print (isiAir(kapasitas, jari2, tinggiAir))
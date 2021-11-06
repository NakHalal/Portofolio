phi = 3.14
def hitungVolumeSilinder(r, t):
    #lengkapi fungsi berikut
    vol = phi * r ** 2 * t
    return vol

jari = int(input())
tinggi = int(input())

print(hitungVolumeSilinder(jari, tinggi))
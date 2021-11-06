phi = 3.14
def hitungVolumeSilinder(r, t):
    #lengkapi fungsi berikut
    vol = phi * r ** 2 * t
    return vol

def isiAir():
    teko = int(input())
    jari = int(input())
    tinggi = list(map(int, input().split()))
    for g in range(len(tinggi)):
        teko -= hitungVolumeSilinder(jari, tinggi[g]) 
        if teko < 0:
            break
        g += 1
    print(g)
isiAir()
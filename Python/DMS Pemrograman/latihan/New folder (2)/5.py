jam = 0
menit = 0
detik = int(input())

def konversiWaktu():
    global jam, menit, detik
    jam = detik // 3600
    detik = detik - (3600*jam)
    menit = detik // 60
    detik = detik - (60*menit)
    #lengkapi fungsi berikut
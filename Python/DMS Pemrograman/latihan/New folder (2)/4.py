detik = int(input())
def konversiWaktu(a):
   jam = a // 3600
   a = a % 3600
   menit = a // 60
   a = a % 60 
   detik = a
   return (jam, menit, detik)

konversiWaktu(detik)
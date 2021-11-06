'''text = 'seratus dua puluh ribu rupiah (Rp 125.000), dan lima puluh rupiah (Rp 50)'
newtext = text.replace('(', '[')
print(newtext)
newtext = newtext.replace(')', ']')
print(newtext)'''

rupiah = "seratus dua puluh ribu rupiah (Rp 125.000), dan lima puluh rupiah (Rp 50)"
rupiahdollar = rupiah.replace ("Rp", "$")
print(rupiahdollar)

rupiahtitik = "seratus dua puluh ribu rupiah (Rp 125.000), dan lima puluh rupiah (Rp 50)"
rupiah_titik = rupiahtitik.replace(" ", ".")
print(rupiah_titik)
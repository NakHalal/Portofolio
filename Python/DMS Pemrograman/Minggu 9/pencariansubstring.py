text = 'seratus dua puluh ribu rupiah (Rp 125.000)'

start = text.find('(Rp')
end = text.find(')')
print(start, end)

nominal = text[start+1:end]
print(nominal)
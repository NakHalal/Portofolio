kalimat = input().split()
cari = input().split()
bracket = []

for x in cari:
    a = kalimat.count(x)
    if kalimat.count(x) == 0:
        a = "None"
        bracket.append(a)
    else:
        bracket.append(a)

for i in bracket:
    print(i, end = " ")
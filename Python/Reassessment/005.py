A = ""
cek = ''
while cek != "finish":
    if cek == '':
        A = '{}'.format(A)
    elif A == '':
        A = '{}'.format(cek)
    else:
        A = '{} {}'.format(A, cek)
    cek = input()
print(A)
def check(L):
    z = type(L[0])
    for x in L:
        assert type(x) == z, "Tipe Data Tidak Seragam"
    return "OK"

L1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("L1", check(L1))
L2 = [True, False, True, False]
print('L2', check(L2))
L3 = ['a', 'b', True, 5, 'd', 'e', 'f', 'g']
print('L3', check(L3))
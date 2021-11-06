a = int(input())
n = []
v = []
b = {}
for i in range(a):
    x,y = input().split(' ')
    y = int(y)
    n.append(x)
    v.append(y)

m = int(max(v))
i = v.index(max(v))
print(n[i] , 'terpilih dengan {} suara'.format(m))
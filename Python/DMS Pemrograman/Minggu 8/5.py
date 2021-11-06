a = set([i for i in input().split()])
b = set([i for i in input().split()])
c = []

for x in a:
    if x in b:
        c.append(x)
print(len(c))
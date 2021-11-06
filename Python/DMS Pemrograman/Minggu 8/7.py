a = set([i for i in input().split()])
b = set([i for i in input().split()])
c = set([i for i in a])

c.update(b)

print(len(c))

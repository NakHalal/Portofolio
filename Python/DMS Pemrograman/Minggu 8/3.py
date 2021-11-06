data = tuple([int(i) for i in input().split()])
x = int(input())

count = 0
for d in data:
    if (d % x == 0):
        count += 1
print(count)

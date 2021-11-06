def truncate(x):
    global val, den
    if val % x != 0:
        val = val - (val % x)

val=int(input())
den=int(input())

print(val, den)
truncate(den)
print(val, den)

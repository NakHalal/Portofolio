n = int(input())
suara = [int(i) for i in input().split()]

win = [0 for i in range(n + 1)]

for s in suara:
    win[s] += 1

winPoint = max(win)
winner = []

for i in range(n + 1):
    if (win[i] == winPoint):
        winner.append(i)

if(len(winner) == 1):
    print("Pemenang pemilu adalah peserta dengan nomor {}".format(winner[0]))
else:
    print("voting ulang")

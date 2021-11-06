gubernur = ["", 0]

def hitung(gubernur, calon, vote):
  if (vote > gubernur[1]):
    gubernur[0] = calon
    gubernur[1] = vote

N = int(input())
for i in range(N):
  calon, vote = input().split(" ")
  vote = int(vote)
  hitung(gubernur, calon, vote)
print (gubernur[0], "terpilih dengan", gubernur[1], "suara")
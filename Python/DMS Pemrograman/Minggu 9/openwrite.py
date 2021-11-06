'''fileopen = open ("initext.txt")
for i in fileopen:
    print(i,end="")'''

'''fileopen = open ("initext.txt","w")
fileopen.write("Halo guys david disini")
fileopen.close()
print("write telah selesai")

for i in fileopen:
    print(i,end="")'''

fileopen = "initext.txt"
f = open (fileopen,"w")
str_list = ["Halo guys david disini", "Hai semua nama gw ewing", "Dimas ganteng"]
teks = "/".join(str_list) + "\nalohaa"
f.write(teks)
f.close
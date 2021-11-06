A=input("lebih suka gunung atau pantai? (gunung/pantai/abstain) ")
B=input("lebih suka bepergian jauh atau yang dekat-dekat saja? (jauh/dekat/abstain) ")
C=input("budget yang dipunya untuk liburan? ")

if A == "abstain" or B == "abstain":
    print("dirumahaja")
elif A == "gunung" and C > "2000000" and B == "dekat":
    print("pergi glamping ke lembang")
elif A == "gunung" and C <= "2000000":
    print("mendaki gunung gede")
elif A == "pantai" and C > "5000000":
    print("liburan ke bali")
elif A == "pantai" and C <= "5000000":
    print("liburan ke pangandaran")


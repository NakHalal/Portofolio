A=input("lebih suka bepergian jauh atau yang dekat-dekat saja? (jauh/dekat/abstain)")
B=input("apakah suka kesenian (ya/tidak)")
C=input("apakah suka pergi ke museum (ya/tidak)")

if C == "ya" and A == "dekat" and B == "ya":
    print("selasar sunaryo")
elif C == "ya" and A == "dekat" and B == "tidak":
    print("museum geologi")
elif (A == "dekat" or A == "abstain") and B == "ya":
    print("saung angklung mang udjo")
elif A == "jauh" and B == "ya":
    print("prambanan")
else:
    print("tidak ada saran")

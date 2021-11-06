"""
Buatlah sebuah program yang akan menerima input berupa dua buah string sebagai jawaban
pertanyaan berikut:
1) Apakah hari ini ada UTS?(ya/tidak)
2) Apakah hari ini hujan?(ya/tidak)

Kemudian program akan menge-outputkan:
- &#39;tetap semangat belajar&#39;, jika jawaban pertanyaan pertama DAN kedua adalah &#39;ya&#39;
- &#39;mau hujan mau panas tetap semangat belajar&#39;, jika jawaban pertanyaan pertama adalah &#39;ya&#39;
"""

tanya1 = input("Apakah hari ini ada UTS?(ya/tidak)")
tanya2 = input("Apakah hari ini hujan?(ya/tidak)")

if tanya1 == ("ya") and tanya2 == ("ya"):
    print("tetap semangat belajar")
elif tanya1 == ("ya") and tanya2 ==("tidak"):
    print("mau hujan mau panas tetap semangat belajar")

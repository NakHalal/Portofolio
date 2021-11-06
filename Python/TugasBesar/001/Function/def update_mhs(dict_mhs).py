def update_mhs(dict_mhs):
    '''
    Minta nim mahasiswa. Jika nim terdaftar, tampilkan data eksisting.
    Minta data baru, namun jika field tidak ingin diupdate user dapat mengosongkan saja dan field tersebut tidak akan diubah.
    Jika nim tidak ada, tampilkan pesan
    '''
    print('----Fungsi "update_mhs" dijalankan----')
    #jawaban anda di bawah ini
    IPT = input("Masukkan NIM \t: ")
    QWE = dict(dict_mhs["data"])
    for AB in QWE.keys():
        #print(QWE.keys())
        if IPT == AB:
            TRE = QWE[IPT]
            print("Data ditemukan.")
            print("Nama     \t:", TRE["Nama"])
            print("Email    \t:", TRE["Email"])
            print("Password \t:", TRE["Password"])
            print()
            print("Masukkan data baru, jika tidak ingin diupdate, biarkan kosong.")
            NB = input("Masukkan Nama     \t: ")
            EB = input("Masukkan Email    \t: ")
            PB = input("Masukkan Password \t: ")
            if NB != "":
                TRE["Nama"] = NB
            if EB != "":
                TRE["Email"] = EB
            if PB != "":
                TRE["Password"] = PB

    try:
        input("Tekan Enter untuk kembali ke menu utama...")
    except Exception:
        pass
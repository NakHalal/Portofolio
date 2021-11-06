def update_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Tampilkan jawaban eksisting, lalu minta jawaban baru. Jika tidak jadi update cukup dikosongkan maka tidak dilakukan perubahan jawaban.
    '''
    print('----Fungsi "update_submission" dijalankan----')
    nim = str(nim)
    print()
    try:
        for WQA in range(1, len(list_topic)+1):
            PQW = WQA - 1
            WQB = dict(list_topic[PQW])
            print("{}: ".format(WQA), WQB['Title'])
    except Exception:
        pass
    else:
        try:
            WQE = int(input("Masukkan Nomor Topic \t: "))
            WQR = WQE - 1
            ZZZ = list_topic[WQR]
        except Exception:
            pass
        else:
            print()
            print("Berikut adalah list assignment \t: ")
            print("ID \t| Title \t\t| Type \t\t| Description \t\t")
            print("—"*75)
            for WQA in range(1, len(list_topic)+1):
                PQW = WQA - 1
                WQB = dict(list_topic[WQR])
            for RTX in WQB['Activities']:
                if dict_activity[RTX]['Type'] == 'assignment':
                    print(RTX, ' \t|', dict_activity[RTX]['Title'], ' \t|', dict_activity[RTX]['Type'], " \t|", dict_activity[RTX]['Description'])
            try:
                LKJ = int(input("Masukkan ID Assginment \t: "))
                dict_submission[LKJ][nim]
            except Exception:
                pass
            else:
                if LKJ in WQB['Activities']:
                    print()
                    print("Jawaban Sebelumnya \t: ")
                    print(dict_submission[LKJ][nim])
                    print()
                    KHJ = input("Masukkan jawaban baru atau kosongkan jika batal update \t: ")
                    if KHJ != "":
                        dict_submission[LKJ][nim] = KHJ
                    else:
                        pass
                    print()
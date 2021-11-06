def udpate_activity(list_topic, dict_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "udpate_activity" dijalankan----')
    #jawaban anda di bawah ini
    HS = len(list_topic)
    HS += 1
    for P in range(1,HS):
        K = P - 1
        print("{}: ".format(P), list_topic[K]['Title'])
    try:
        JHG = int(input("Masukkan nomor topic yang ingin diupdate activity-nya: "))
    except Exception:
        pass
    else:
        if JHG <= len(list_topic) and JHG > 0:
            JHG -= 1
            print("\nList Activity: ")
            print("ID \t| Title \t\t| Type \t\t| Description \t")
            print("—"*75)
            for AS in list_topic[JHG]["Activities"]:
                print(AS, " \t|", dict_activity[AS]['Title'], " \t|", dict_activity[AS]["Type"], " \t|", dict_activity[AS]["Description"])
            print()
            try:
                BGH = int(input("Masukkan ID activity yang akan diupdate: "))
            except Exception:
                pass
            else:
                if BGH in list_topic[JHG]["Activities"]:
                    print("Masukkan data baru. Kosongkan jika tidak ingin diubah.")
                    TUP = input("Masukkan Title: ")
                    if TUP != "":
                        dict_activity[AS]["Title"] = TUP
                    YUP = input("Masukkan Type (assignment/material): ")
                    if YUP != "":
                        dict_activity[AS]["Type"] = YUP
                    DUP = input("Masukkan Description activity: ")
                    if DUP != "":
                        dict_activity[AS]["Description"] = DUP
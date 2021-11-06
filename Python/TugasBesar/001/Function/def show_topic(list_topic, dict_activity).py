def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    #jawaban anda di bawah ini

    print("")
    list_topic = list(list_topic)
    for a in list_topic:
        VD = dict(a)
        print("Title\t\t:", VD["Title"])
        print("Description\t:", VD["Description"])
        print("List Activity\t:")
        print("ID\t| Title\t\t\t| Type\t\t| Description\t\t")
        print("—"*75)
        for i in VD["Activities"]:
            DPX = dict(dict_activity[i])
            print(i, "\t|", DPX["Title"], "\t|", DPX["Type"], "\t|", DPX["Description"])
        print("")
    
    try:
        input("Tekan Enter untuk kembali ke menu utama...")
    except Exception:
        pass
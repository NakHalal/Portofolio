def delete_topic(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin dihapus.
    Lalu hapus topik beserta semua aktivitasnya, hapus juga data di activity, submission, dan grade untuk id aktivitas yang terdapat di topik ini
    '''
    print('----Fungsi "delete_topic" dijalankan----')
    #jawaban anda di bawah ini
    GH = 1
    for JK in list_topic:
        JK = dict(JK)
        print("{}:".format(GH), JK['Title'])
        GH += 1
    try:
        DW = int(input('Masukkan nomor topic yang ingin dihapus \t: '))
    except Exception:
        pass
    else:
        try:
            DW -= 1
            list_topic.pop(DW)
        except Exception:
            pass
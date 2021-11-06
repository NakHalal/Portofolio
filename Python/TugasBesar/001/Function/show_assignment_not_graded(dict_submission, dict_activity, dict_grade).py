def show_assignment_not_graded(dict_submission, dict_activity, dict_grade):
    '''
    Tampilkan setiap data activity assignment yang memiliki setidaknya satu submission mahasiswa yang belum dinilai
    '''
    print('----Fungsi "show_assignment_not_graded" dijalankan----')
    #jawaban anda di bawah ini
    print('List assignment yang memiliki submission yang belum lengkap nilainya')
    print("ID \t| Title \t")
    print("—"*50)
    JNM = len(dict_mhs['data'])
    for PK in dict_activity.keys():
        if 'assignment' in dict_activity[PK].get('Type'):
            if JNM != len(dict_submission[PK]):
                print(PK, '\t|', dict_activity[PK]['Title'], '\t')      
    print()
    try:
        input("Tekan Enter untuk kembali ke menu utama...")
    except Exception:
        pass
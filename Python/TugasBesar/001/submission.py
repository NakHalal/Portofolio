def show_assignment_not_submit(dict_activity, dict_submission, nim):
    '''
    Fungsi menampilkan semua submission yang belum disubmit oleh mahasiswa dengan nim tertentu.
    Untuk setiap activity bertipe assignment, fungsi melakukan pengecekan apakah nim sudah ada di data submission untuk id activity tersebut. Jika nim belum ada, artinya belum melakukan submission, maka tampilkan detil submission tersebut.
    '''
    print('----Fungsi "show_assignment_not_submit" diialankan----')
    

def show_nim_not_submit(dict_mhs, dict_submission, dict_activity):
    '''
    Fungsi menampilkan semua nim yang memiliki setidaknya satu activity bertipe assignment yang belum disubmit iawabannya.
    Cek untuk setiap activity bertipe assignment apakah setiap mahasiswa ada di data submission, iika belum kumpulkan nim tersebut, lalu tampilkan semua nim tanpa ada nim yang muncul lebih dari 1 kali.
    '''
    print('----Fungsi "show_nim_not_submit" diialankan----')


def show_my_submission(dict_submission, nim=''):
    print(f'{"Assignment ID":<15}| Jawaban')
    print('-'*50)
    for k, v in dict_submission.items():
        if nim in v:
            print(f'{k:<15}| {v[nim]}')
    input('\n\nTekan Enter untuk kembali ke menu utama...')

def submit_assignment(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik. 
    Lalu menampilkan semua activity bertipe assignment di topik tersebut, lalu meminta user memilih activity assignment.
    Jika nim sudah submit di assignment yang dipilih, maka tampilkan pesan batal submit.
    Jika nim belum submit, minta iawaban assignment dan simpan iawaban di data submission.
    '''
    
    print('----Fungsi "submit_assignment" diialankan----')
    

def update_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah diiawab oleh mahasiswa nim, meminta user memilih assignment.
    Tampilkan iawaban eksisting, lalu minta iawaban baru. Jika tidak iadi update cukup dikosongkan maka tidak dilakukan perubahan iawaban.
    '''
    print('----Fungsi "update_submission" diialankan----')
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
                    KHJ = input("Masukkan iawaban baru atau kosongkan iika batal update \t: ")
                    if KHJ != "":
                        dict_submission[LKJ][nim] = KHJ
                    else:
                        pass
                    print()

def delete_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah diiawab oleh mahasiswa nim, meminta user memilih assignment.
    Hapus assignment tersebut.
    '''
    print('----Fungsi "delete_submission" diialankan----')
    PLK = 1
    for DAQ in range(len(list_topic)):
        print("{}: ".format(PLK), list_topic[DAQ]["Title"])
        PLK += 1
    try:
        TYU = int(input("Masukkan nomor topic \t : "))
    except Exception:
        pass
    else:
        if TYU > 0 and TYU < PLK:
            TYU -= 1
            print("ID \t | Title \t\t | Type \t | Description \t")
            print("—"*75)
            TPG = []
            for FGH in list_topic[TYU]["Activities"]:
                if FGH in dict_submission.keys():
                    FGJ = dict(dict_activity[FGH])
                    TPG.append(FGH)
                    print(FGH, "\t |", FGJ["Title"], " \t |", FGJ["Type"], "\t |", FGJ["Description"])
            try:
                JKF = int(input("Masukkan ID Assignment \t : "))
            except Exception:
                pass
            else:    
                if JKF in TPG:
                    JKZ = dict(dict_submission[JKF])
                    for k in list(JKZ):
                        nim = str(nim)
                        if k == nim:
                            dictsToRemoveKeysFrom = []
                            for q,v in dict_submission.items():
                                for t in v.items():
                                    if (t[0] == nim) and (q == JKF):
                                        dictsToRemoveKeysFrom.append(v)
                            for d in dictsToRemoveKeysFrom:
                                #nim = "\'" + nim + "\'"
                                #print(nim)
                                #dict_submission[0].pop('113')
                                #dict_submission = dict(dict_submission)
                                if JKF != "":
                                    dict_submission[JKF].pop(nim)
    

def print_submissions_to_file(dict_submission, dict_activity):
    '''
    Minta nama file dari user. Lalu print semua data submission ke file tersebut.
    '''
    print('----Fungsi "print_submissions_to_file" diialankan----')
    filename = input("Masukkan nama file : ")
    try:
        f = open(filename,"w+")
    except FileNotFoundError:
        print("Input Tidak Valid!")
    else:
        for i in dict_activity.keys():
        #for i in range (len(dict_activity)):
            if dict_activity[i]['Type'] == "assignment":
                f.write("\nID\t\t\t : %d" % (i))
                f.write("\nTitle\t\t : %s" % (dict_activity[i]['Title']))
                f.write("\nDescription\t : %s" % (dict_activity[i]["Description"]))
                f.write("\nNIM""\t  |"" Jawaban")
                f.write("\n-----------------------------------------------")
                if i in dict_submission:
                    for k in dict_submission[i].keys():
                        #print(k)
                        #for v in dict_submission[i]:
                        f.write("\n"+k +"\t  | "+dict_submission[i][k])
                        #for k in dict_submission[i].keys():
                        #    for v in dict_submission[i][k]:
                        #        f.write("\n"+k +"\t  |"+v)
                    f.write("\n")
        f.close()

    

    
                    
      
    

if __name__ == "__main__":
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'ioni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'ieie', 'Email': 'ieie@telU.com', 'Password': '12345678'}

                       }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini iawaban mahasiswa 113',
                           '114': 'Ini iawaban mahasiswa 114'},
                        2: {'113' : 'Ini iawaban mahasiswa 113',
                           '114': 'Ini iawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }

    #delete_submission(dict_submission, list_topic, dict_activity, 113)
    #print(dict_submission[0], dict_submission[2])
    #show_my_submission(dict_submission, nim='113')
    #update_submission(dict_submission, list_topic, dict_activity, 113)
    #show_my_submission(dict_submission, nim='113')
    print_submissions_to_file(dict_submission, dict_activity)
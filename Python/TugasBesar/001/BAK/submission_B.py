def show_assignment_not_submit(dict_activity, dict_submission, nim):
    '''
    Fungsi menampilkan semua submission yang belum disubmit oleh mahasiswa dengan nim tertentu.
    Untuk setiap activity bertipe assignment, fungsi melakukan pengecekan apakah nim sudah ada di data submission untuk id activity tersebut. Jika nim belum ada, artinya belum melakukan submission, maka tampilkan detil submission tersebut.
    '''
    print('----Fungsi "show_assignment_not_submit" dijalankan----')
    

def show_nim_not_submit(dict_mhs, dict_submission, dict_activity):
    '''
    Fungsi menampilkan semua nim yang memiliki setidaknya satu activity bertipe assignment yang belum disubmit jawabannya.
    Cek untuk setiap activity bertipe assignment apakah setiap mahasiswa ada di data submission, jika belum kumpulkan nim tersebut, lalu tampilkan semua nim tanpa ada nim yang muncul lebih dari 1 kali.
    '''
    print('----Fungsi "show_nim_not_submit" dijalankan----')


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
    Jika nim belum submit, minta jawaban assignment dan simpan jawaban di data submission.
    '''
    
    print('----Fungsi "submit_assignment" dijalankan----')
    

def update_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Tampilkan jawaban eksisting, lalu minta jawaban baru. Jika tidak jadi update cukup dikosongkan maka tidak dilakukan perubahan jawaban.
    '''
    print('----Fungsi "update_submission" dijalankan----')


def delete_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Hapus assignment tersebut.
    '''
    print('----Fungsi "delete_submission" dijalankan----')
    PLK = 1
    for DAQ in range(len(list_topic)):
        print("{}: ".format(PLK), list_topic[DAQ]["Title"])
        PLK += 1
    try:
        TYU = int(input("Masukkan nomor topic \t : "))
    except Exception:
        pass
    else:
        DAQ += 1
        if TYU > 0 and TYU < DAQ:
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
                                d.pop(nim)

def print_submissions_to_file(dict_submission, dict_activity):
    '''
    Minta nama file dari user. Lalu print semua data submission ke file tersebut.
    '''
    print('----Fungsi "print_submissions_to_file" dijalankan----')

    

    
                    
      
    

if __name__ == "__main__":
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                       }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]},
                    {'Title': 'Dummy Topic 3', 'Description': 'Ini deskripsi topic 3', 'Activities':[3]},
                    {'Title': 'Dummy Topic 4', 'Description': 'Ini deskripsi topic 2', 'Activities':[4]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'assignment', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'},
                         3: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        1: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        3: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}   
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }
    delete_submission(dict_submission, list_topic, dict_activity, 114)


    
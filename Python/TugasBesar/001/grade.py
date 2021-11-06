def show_all_grade(dict_grade, dict_activity):
    '''
    Tampilkan setiap  aktifitas beserta list nilai mahasiswanya
    '''
    print('----Fungsi "show_all_grade" dijalankan----')
    for k, v in dict_grade.items():
        print(f'ID\t: {k}')
        print(f'Title\t:{dict_activity[k]["Title"]}')
        print(f'Nilai semua mahasiswa: ')
        print(f'{"NIM":<10}|Nilai')
        print('-'*15)
        for nim, nilai in v.items():
            print(f'{nim:<10}|{nilai}')
        print()

    input('\n\nTekan Enter untuk kembali ke menu...')


def show_mhs_not_graded(dict_submission, dict_grade):
    '''
    Tampilkan setiap nim mahasiswa yang memiliki setidaknya satu submission yang belum dinilai
    '''
    print('----Fungsi "show_mhs_not_graded" dijalankan----')
    #jawaban anda di bawah ini


def add_grade_by_mhs(dict_submission, dict_activity, dict_grade):
    '''
    Minta nim 1 mahasiswa
    Cek nim tersebut di semua submission, lalu cek apakah sudah ada nilai. Jika belum, tampilkan detil assignment.
    Tampilkan jawaban mahasiswa, lalu minta nilainya.
    '''
    print('----Fungsi "add_grade_by_mhs" dijalankan----')
    #jawaban anda di bawah ini
    KKK = input("Masukkan NIM yang ingin dinilai: ")
    NIMFOUND = 0
    IDFOUND = 0
    CHECK = "NOTOK"
    SBFOUND = "NOTOK"
    RT = "NOTFOUND"
    Q = []
    W = {}
    E = {}
    for i in dict_mhs['data'].keys():
        if KKK == i:
            NIMFOUND = 1
    if NIMFOUND == 1:
        for j in dict_submission:
            for k in dict_grade:
                if j == k:
                    Q.append(j)
                    IDFOUND = 1
    if IDFOUND == 1:
        for i in Q:
            for j in dict_submission[i]:
                for k in dict_grade[i]:
                    if j == k:
                        if j == KKK:
                            W[i] = j
                            CHECK = "OK"
    if CHECK == "OK":
        for i in dict_submission:
            for j in dict_submission[i].keys():
                for k in dict_grade[i]:
                    E[i] = j
                    SBFOUND = "OK"
                    RSLT = dict(E)
    if SBFOUND == "OK":
        for i, j in W.items():
            for k, l in E.items():
                if i == k:
                    RSLT.pop(i)
                    RT = "FOUND"
    print(E)
    print(W)
    if RT == "FOUND":
        for i, j in RSLT.items():
            print("Detil Assignment...")
            print("ID \t\t:", i, "\nTitle \t\t:", dict_activity[i]['Title'], "\nDescription \t:", dict_activity[i]['Description'])
            print("\nJawaban mahasiswa:")
            print(dict_submission[i][j], '\n')
            try:
                NEW = int(input('Masukkan nilai (0-100):'))
                print()
            except Exception:
                pass
            else:
                if NEW >= 0 and NEW <= 100:
                    dict_grade[i][j] = NEW



'''
        for j in dict_submission.keys():
            for k in dict_submission[j].keys():
                try:
                    if str(KKK) == str(k):
                        for B in dict_grade.keys():
                            for C in dict_grade[B].keys():
                                if KKK == C:
                                    for FG in dict_submission[j]:
                                        for GH in dict_grade[j]:
                                            if FG == GH:
                                                print("ID \t:", B, C, FG)
                except Exception:
                    pass
'''
        
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

def add_grade_by_assignment(dict_submission, dict_grade):
    '''
    Minta ID assignment yang ingin dinilai.
    Tampilkan data nim mahasiswa beserta jawaban yang belum dinilai, lalu minta nilainya
    '''
    print('----Fungsi "add_grade_by_assignment" dijalankan----')
    #jawaban anda di bawah ini
    try:
        TRD = int(input("Masukkan ID assignment yang ingin dinilai \t: "))
    except Exception:
        pass
    else:
        if TRD in dict_submission.keys():
            print("NIM \t| Jawaban \t")
            print("—"*75)
            for Q in dict_submission.keys():
                for W in dict_submission[Q]:
                    if TRD == Q:
                        print(W, " \t|", dict_submission[Q][W])
                        try:
                            SAD = int(input("Masukkan nilai (0-100) \t: "))
                        except Exception:
                            pass
                        else:
                            if 0 <= SAD <= 100:
                                try:
                                    dict_grade[Q][W] = SAD
                                except KeyError:
                                    dict_grade[Q] = {}
                                    dict_grade[Q][W] = SAD
                                else:
                                    dict_grade[Q][W] = SAD
                                
                            
                        


    #print(dict_grade)
    #print("\n")
    try:
        input("Tekan Enter untuk kembali ke menu utama...")
    except Exception:
        pass

def report_by_assignment(dict_submission, dict_activity, dict_grade):
    '''
    Tampilkan data rekapan untuk tiap assignment, berupa nilai rata-rata dari semua mahasiswa, banyaknya submission di assignment tersebut, dan banyak submission yang sudah dinilai
    '''
    print('----Fungsi "report_by_assignment" dijalankan----')
    #jawaban anda di bawah ini
    print("ID \t| Title \t\t| Rata-Rata \t| #Submission \t| #Dinilai \t")
    print("—"*75)
    for Z in dict_activity:
        if "assignment" in dict_activity[Z].values():
            for k, v in dict_activity[Z].items():
                if k == "Title":
                    try:
                        dict_grade[Z]
                    except KeyError:
                        LN = 0
                    except Exception:
                        pass
                    else:
                        LN = len(dict_grade[Z].keys())
                        TTL = 0
                    try:
                        dict_grade[Z]
                    except KeyError:
                        rata = 0
                    except Exception:
                        pass
                    else:
                        for PASYA in dict_grade[Z]:
                            TTL +=  dict_grade[Z][PASYA]
                            rata = TTL / LN
                    try:
                        dict_submission[Z]
                    except KeyError:
                        LM = 0
                    except Exception:
                        pass
                    else:
                        LM = len(list(dict_submission[Z].keys()))
                    try:
                        dict_grade[Z]
                    except KeyError:
                        LK = 0
                    except Exception:
                        pass
                    else:
                        LK = len(dict_grade[Z])
                    print(Z, "\t|", v, "\t|", rata, "    \t|", LM, "\t\t|", LK)
            
        

def report_by_mhs(dict_submission, dict_grade):
    '''
    Tampilkan data rekapan untuk tiap mahasiswa, berupa nilai rata-rata untuk semua assignment, banyaknya submission oleh mahasiswa, dan banyaknya submission mahasiswa tersebut yang sudah dinilai.
    '''
    print('----Fungsi "report_by_mhs" dijalankan----')
    #jawaban anda di bawah ini
    

def print_grade_to_file(dict_grade, dict_activity):
    '''
    Minta nama file.
    Tulis semua data grade ke file.
    '''
    print('----Fungsi "print_grade_to_file" dijalankan----')
    #jawaban anda di bawah ini

    

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
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        3: {'114':'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100, '114' : 80},
                  2: {'113' : 56}
                        
                  }
    #report_by_assignment(dict_submission, dict_activity, dict_grade)
    #show_assignment_not_graded(dict_submission, dict_activity, dict_grade)
    add_grade_by_mhs(dict_submission, dict_activity, dict_grade)
    #print(dict_grade)
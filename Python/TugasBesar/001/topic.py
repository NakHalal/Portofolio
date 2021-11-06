def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    #jawaban anda di bawah ini
    print("")
    list_topic = list(list_topic)
    for CTD in list_topic:
        DLT = dict(CTD)
        print("Title\t\t:", DLT["Title"])
        print("Description\t:", DLT["Description"])
        print("List Activity\t:")
        print("ID\t| Title\t\t\t\t| Type\t\t| Description\t\t\t")
        print("—"*100)
        for CATV in DLT["Activities"]:
            DATV = dict(dict_activity[CATV])
            print(CATV, "\t|", DATV["Title"], "\t\t|", DATV["Type"], "\t|", DATV["Description"])
        print("")
    
    try:
        input("Tekan Enter Untuk Kembali ke Menu Utama...")
    except Exception:
        pass
    

def add_topic(list_topic, dict_activity, id_activity):
    '''
    Meminta data topik baru. Menambahkan topik baru ke list_topic.
    Tanya jika ingin sekaligus menambahkan actifitas. Jika menambahkan aktifitas, naikkan counter id_activity dengan 1,
    baru dijadikan sebagai key activity baru.

    Return id_activity yang terakhir digunakan

    '''
    print('----Fungsi "add_topic" dijalankan----')
    #jawaban anda di bawah ini
    

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

def update_topic(list_topic):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Tampilkan data eksisting.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "update_topic" dijalankan----')
    #jawaban anda di bawah ini
    
    

def add_activity(list_topic, dict_activity, id_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin tambah aktifitas.
    Minta data aktifitas baru, tambahkan counter id_activity dengan 1, lalu tambahkan ke dalam dict_activity.
    Tambahkan juga id_activity ke dalam list aktifitas topik.
    Tanya jika ingin menambah aktifitas lagi

    Return: id_activity yang terakhir digunakan
    '''

    print('----Fungsi "add_activity" dijalankan----')
    #jawaban anda di bawah ini

    

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
    
def delete_activity(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, minta inputan topik. 
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Hapus activity, submission, dan grade dengan id activity yang dipilih
    '''
    print('----Fungsi "delete_activity" dijalankan----')
    #jawaban anda di bawah ini
    Q = 1
    for i in list_topic:
        P = dict(i)
        print("{}: ".format(Q), i['Title'])
        Q += 1
    try:
        NTD = int(input("Masukkan Nomor Topic yang Ingin Didelete Activitynya: "))
    except Exception:
        print("Input Tidak Sesuai!")
    else:
        if NTD in range(1,Q):
            NTX = NTD - 1
            print("List Activity: ")
            print("ID \t| Title \t\t| Type \t\t| Description \t")
            print("—"*100)
            JGX = dict(list_topic[NTX])
            for j in JGX['Activities']:
                print(j, " \t|", dict_activity[j]['Title'], ' \t|', dict_activity[j]['Type'], " \t|", dict_activity[j]['Description'])
            try:
                HPS = int(input("Masukkan ID Activity yang Akan Dihapus: "))
            except Exception:
                print("Input Tidak Sesuai!")
            else:
                try:
                    dict_activity.pop(HPS)
                except Exception:
                    pass
                try:
                    dict_submission.pop(HPS)
                except Exception:
                    pass
                try:
                    dict_grade.pop(HPS)
                except Exception:
                    pass
                
                print("Delete Activity Selesai.")
        else:
            print("Input Tidak Sesuai!")

    try:
        input("\nTekan Enter Untuk Kembali ke Menu Utama...")
    except Exception:
        pass

      

    



def print_topic_to_file(list_topic, dict_activity):
    '''
    Minta nama file.
    Print setiap detail topik, beserta list aktifitasnya ke file.
    '''

    print('----Fungsi "print_topic_to_file" dijalankan----')
    #jawaban anda di bawah ini
    NF = input("Masukkan nama file: ")
    f = open(NF, 'w+')
    print(f.read(), end='')

    #list_topic = list(list_topic)
    for a in list_topic:
        VD = dict(a)
        S001 = "Title\t\t:", VD["Title"], "\n"
        J001 = ' '.join(S001)
        f.write(J001)
        S002 = "Description\t:", VD["Description"], "\n"
        J002 = ' '.join(S002)
        f.write(J002)
        S003 = "List Activity\t:", "\n"
        J003 = ' '.join(S003)
        f.write(J003)
        S004 = "ID\t|", "Title \t\t\t|", "Type\t\t|", "Description\t\t", "\n"
        J004 = ' '.join(S004)
        f.write(J004)
        S005 = "---------------------------------------------------------------------------------------------", "\n"
        J005 = ' '.join(S005)
        f.write(J005)
        for i in VD["Activities"]:
            DPX = dict(dict_activity[i])
            #S006= i, "\t|", DPX["Title"], "\t|", DPX["Type"], "\t|", DPX["Description"], "\n"
            J006= "{} \t| {}  \t| {} \t| {} \n".format(i, DPX["Title"], DPX["Type"], DPX["Description"])
            LKJ = []
            #for j in S006:
            #    A = str(j)
            #    LKJ.append(A)
            #J006 = ' '.join(LKJ)
            #J006 = "{}".format(DPX["Title"])
            f.write(J006)
        f.write("\n")
    print('Print topic dan activity ke file berhasil\n')
    
    try:
        input("Tekan Enter Untuk Kembali ke Menu Utama...")
    except Exception:
        pass

    




    
if __name__ == "__main__":
    #type_activity = ['assignment', 'material']
    #id_activity adalah variable global untuk id unik semua activity di semua topic
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
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }
    #print(list_topic)

    #print_topic_to_file(list_topic, dict_activity)
    #delete_topic(list_topic, dict_activity, dict_submission, dict_grade)
    show_topic(list_topic, dict_activity)
    #print(dict_activity)
    #udpate_activity(list_topic, dict_activity)
    #print(dict_activity)
    #print(dict_activity)
    #print(dict_submission)
    #print(dict_grade)
    #print()
    #delete_activity(list_topic, dict_activity, dict_submission, dict_grade)
    #print(dict_activity)
    #print(dict_submission)
    #print(dict_grade)
    #print()
def print_to_file(dict_mhs):
    '''
    Print data mahasiswa ke dalam file teks. 1 mahasiswa per baris, dan kolomnya adalah sesuai field, pisahkan dengan tab.
    '''
    print('----Fungsi "print_to_file" dijalankan----')
    #jawaban anda di bawah ini
    NMF = input("Masukkan nama file: ")
    f = open(NMF, 'w+')
    print(f.read(), end='')
    MHS = dict(dict_mhs)
    data = dict(MHS["data"])
    S001 = "Nim", "\t", "Nama", "\t", "Email\t", "\t" , "Password", "\n"
    S002 = ''.join(S001)
    f.write(S002)
    #print(data.keys)
    for key, value in data.items() :
        P = dict(value)
        S003 = key, "\t", P["Nama"], "\t", P["Email"], "\t", P["Password"], '\n'
        S004 = ''.join(S003)
        f.write(S004)
    f.close()
    print('Penyimpanan berhasil\n')
    
    try:
        input("Tekan Enter untuk kembali ke menu utama...")
    except Exception:
        pass
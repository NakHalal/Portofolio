#include "menu.h"

void loopThis(List &NH)
{
    string pilihan;

    pilihan = select_menu();
    while(pilihan != "0")
    {
        if(pilihan == "1")
        {
            add_N_data(NH);
            
            pause();
        }
        else if(pilihan == "2")
        {
            printListFromFirst(NH);

            pause();
        }
        else if(pilihan == "3")
        {
            printListFromLast(NH);

            pause();
        }
        else if (pilihan == "4")
        {  
            string sub_pilihan;
            adr result = NULL;

            sub_pilihan = subselect_menu_search();
            if (sub_pilihan == "1")
            {
                string nama;

                cout << "Masukkan Nama yang Ingin Dicari: ";
                cin >> nama;

                result = searchAddressByName(NH, nama);
            }
            else if (sub_pilihan == "2")
            {
                int nim;

                cout << "Masukkan NIM yang Ingin Dicari: ";
                cin >> nim;

                result = searchAddressByNIM(NH, nim);
            }
            else if (sub_pilihan == "3")
            {
                float ipk;

                cout << "Masukkan IPK yang Ingin Dicari: ";
                cin >> ipk;

                result = searchAddressByIPK(NH, ipk);
            }
            if (result == NULL && sub_pilihan != "0")
            {
                cout << "Data Mahasiswa Tidak Ditemukan" << endl;
            }
            else if (result != NULL && sub_pilihan != "0")
            {
                cout << "[[ Data Mahasiswa Ditemukan ]]" << endl;
                cout << "Nama: " << result->info.nama << endl;
                cout << "NIM : " << result->info.nim << endl;
                cout << "IPK : " << result->info.ipk << endl;
            }
            pause();
        }
        else if (pilihan == "5")
        {
            cout << "Jumlah Data Mahasiswa: " << countList(NH) << endl;

            pause();
        }
        else if (pilihan == "6")
        {
            string sub_pilihan;
            adr result = NULL;

            sub_pilihan = subselect_menu_search();
            if (sub_pilihan == "1")
            {
                string nama;

                cout << "Masukkan Nama yang Ingin Dihapus: ";
                cin >> nama;

                result = searchAddressByName(NH, nama);
            }
            else if (sub_pilihan == "2")
            {
                int nim;

                cout << "Masukkan NIM yang Ingin Dihapus: ";
                cin >> nim;

                result = searchAddressByNIM(NH, nim);
            }
            else if (sub_pilihan == "3")
            {
                float ipk;

                cout << "Masukkan IPK yang Ingin Dihapus: ";
                cin >> ipk;

                result = searchAddressByIPK(NH, ipk);
            }
            if (result == NULL && sub_pilihan != "0")
            {
                cout << "Data Mahasiswa Tidak Ditemukan" << endl;
            }
            else if (result != NULL && sub_pilihan != "0")
            {
                adr M;
                deleteThis(NH, result, M);
                cout << "[[   Data Mahasiswa Ditemukan   ]]" << endl;
                cout << "Nama: " << result->info.nama << endl;
                cout << "NIM : " << result->info.nim << endl;
                cout << "IPK : " << result->info.ipk << endl;
                cout << "[[ Data Mahasiswa Telah Dihapus ]]" << endl;
            }
            pause();
        }
        else
        {
            cout << "[[ Pilihan Salah ]]" << endl;

            pause();
            pilihan = "-1";
        }
        system("CLS");
        pilihan = select_menu();
    }
}

string select_menu()
{
    cout << "=================== Menu ===================" << endl;
    cout << "| 1. Tambah Data Mahasiswa                 |" << endl;
    cout << "| 2. Tampilkan Data Mahasiswa (Dari Awal)  |" << endl;
    cout << "| 3. Tampilkan Data Mahasiswa (Dari Akhir) |" << endl;
    cout << "| 4. Cari Nama Mahasiswa                   |" << endl;
    cout << "| 5. Hitung Jumlah Data Mahasiswa          |" << endl;
    cout << "| 6. Hapus Data Mahasiswa                  |" << endl;
    cout << "| 0. Selesai                               |" << endl;
    cout << "==================== <3 ====================" << endl;
    cout << endl << "Masukkan Menu: ";

    string input = "";
    cin >> input;
    cout << endl;

    return input;
}

string subselect_menu_search()
{
    system("CLS");
    cout << "============ Eksekusi Berdasarkan: ===========" << endl;
    cout << "| 1. Nama Mahasiswa                          |" << endl;
    cout << "| 2. NIM Mahasiswa                           |" << endl;
    cout << "| 3. IPK Mahasiswa                           |" << endl;
    cout << "| 0. Selesai                                 |" << endl;
    cout << "|                                            |" << endl;
    cout << "| *Data pertama yang ditemukan di List yang  |" << endl;
    cout << "|  akan dieksekusi (jika ada)                |" << endl;
    cout << "===================== <3 =====================" << endl;
    cout << endl << "Masukkan Menu: ";

    string input = "";
    cin >> input;
    cout << endl;

    return input;
}

void pause()
{
    cout << endl;
    cout << "Tekan Enter Untuk Kembali Ke Menu";
    system("pause > nil");
    system("CLS");
}
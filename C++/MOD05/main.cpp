#include "SLL.h"
#include "menu.h"

int main()
{
    string pilihan;
    List ListPeg;
    infotype QWE;
    adr P;

    create_list_1301204459(ListPeg);

    QWE.nama = "Adrian Jordan";
    QWE.NIP = "1301209561";
    QWE.gaji = 9500000;
    new_element_1301204459(QWE, P);
    insert_last_1301204459(ListPeg, P);

    QWE.nama = "Sigit Ernando";
    QWE.NIP = "1301202954";
    QWE.gaji = 9000000;
    new_element_1301204459(QWE, P);
    insert_last_1301204459(ListPeg, P);

    QWE.nama = "Fahdnul Maulina";
    QWE.NIP = "1301202568";
    QWE.gaji = 9700000;
    new_element_1301204459(QWE, P);
    insert_last_1301204459(ListPeg, P);

    QWE.nama = "Priyohadi Rahayu";
    QWE.NIP = "1301204862";
    QWE.gaji = 8700000;
    new_element_1301204459(QWE, P);
    insert_last_1301204459(ListPeg, P);

    QWE.nama = "Yusuf Farishy";
    QWE.NIP = "1301201616";
    QWE.gaji = 7300000;
    new_element_1301204459(QWE, P);
    insert_last_1301204459(ListPeg, P);

    pilihan = select_menu_1301204459();
    while (pilihan != "0")
    {
        if (pilihan == "1")
        {
            add_N_data_1301204459(ListPeg);

            pause_1301204459();
        }
        else if (pilihan == "2")
        {
            show_all_data_1301204459(ListPeg);

            pause_1301204459();
        }
        else if (pilihan == "3")
        {
            string X;
            adr P;

            cout << "Masukkan NIP yang Akan Dicari: ";
            cin >> X;

            P = search_by_NIP_1301204459(ListPeg, X);
            if (P != NULL)
            {
                int N = P->info.gaji;
                string s = thousandSeparatorInt_1301204459(N);
                cout << endl << "[[ NIP Ditemukan ]]" << endl;
                cout << "Nama Pegawai: " << P->info.nama << endl;
                cout << "NIP         : " << P->info.NIP << endl;
                cout << "Gaji        : Rp" << s << ",00" << endl;
            }
            else
            {
                cout << endl << "NIP Tidak Ditemukan!" << endl;
            }

            pause_1301204459();
        }
        else if (pilihan == "4")
        {
            string X;
            adr P;

            cout << "Masukkan NIP yang Akan Dihapus: ";
            cin >> X;

            P = search_by_NIP_1301204459(ListPeg, X);
            if (P != NULL)
            {
                int N = P->info.gaji;
                string s = thousandSeparatorInt_1301204459(N);
                cout << endl << "[[ NIP Ditemukan ]]" << endl;
                cout << "Nama Pegawai: " << P->info.nama << endl;
                cout << "NIP         : " << P->info.NIP << endl;
                cout << "Gaji        : Rp" << s << ",00" << endl;
                delete_Data_1301204459(ListPeg, X);
                cout << endl << "[[ Data Pegawai Telah Dihapus ]]" << endl;
            }
            else
            {
                cout << endl << "NIP Tidak Ditemukan!" << endl;
            }

            pause_1301204459();
        }
        else if (pilihan == "5")
        {
            int JMLPGW = jumlah_pegawai_1301204459(ListPeg);
            cout << "Jumlah Pegawai Saat Ini: " << JMLPGW << " Pegawai" << endl;

            pause_1301204459();
        }
        else if (pilihan == "6")
        {
            int JP = jumlah_pegawai_1301204459(ListPeg);
            int TS = total_salary_1301204459(ListPeg);
            string s = thousandSeparatorInt_1301204459(TS);
            string t = thousandSeparatorInt_1301204459(TS/JP);
            cout << "Total Gaji Pegawai: Rp" << s << ",00" << endl;
            cout << "Rata-Rata Gaji Pegawai: Rp" << t << ",00" << endl;

            pause_1301204459();
        }
        else if (pilihan == "7")
        {
            if (highest_salary_1301204459(ListPeg) != NULL)
            {
                int N = highest_salary_1301204459(ListPeg)->info.gaji;
                string s = thousandSeparatorInt_1301204459(N);
                cout << "[[ Gaji Tertinggi Ditemukan ]]" << endl;
                cout << "Nama Pegawai: " << highest_salary_1301204459(ListPeg)->info.nama << endl;
                cout << "NIP         : " << highest_salary_1301204459(ListPeg)->info.NIP << endl;
                cout << "Gaji        : Rp" << s << ",00" << endl;
            }
            else
            {
                cout << "Tidak Ada Data Pegawai" << endl;
            }
            pause_1301204459();
        }
        else
        {
            cout << "[[ Pilihan Salah ]]" << endl;

            pause_1301204459();
            pilihan = "-1";
        }
        system("CLS");  
        pilihan = select_menu_1301204459();
    }
    cout << "Anda Telah Keluar dari Program" << endl;
    cout << "Tekan Enter Untuk Exit";

    system("pause > nul");
    system("CLS");
    return 0;
}
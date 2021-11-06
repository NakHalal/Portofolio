#include "SLL.h"

int main()
{
    int pilihan = 0;
    adr temp, P;
    List MINE; createList_1301204459(MINE);
    string BAK;

    pilihan = selectMenu_1301204459();
    while(pilihan != 0)
    {
        if(pilihan == 1)
        {
            int x = 0;
            cout << endl << "Jumlah Data yang Akan Ditambahkan: ";
            cin >> x;
            while (x > 0)
            {
                cout << "Masukkan Data Baru: ";
                cin >> BAK;
                P = newElement_1301204459(BAK);
                insertLast_1301204459(MINE, P);
                x--;
            }

            cout << endl;
            cout << "Tekan Enter Untuk Kembali Ke Menu";
            system("pause > nil");
            system("CLS");
        }
        else if(pilihan == 2)
        {
            show_1301204459(MINE);

            cout << endl;
            cout << "Tekan Enter Untuk Kembali Ke Menu";
            system("pause > nil");
            system("CLS");
        }
        else if(pilihan == 3)
        {
            int Z = countAll_1301204459(MINE);
            cout << Z << endl;

            cout << endl;
            cout << "Tekan Enter Untuk Kembali Ke Menu";
            system("pause > nil");
            system("CLS");
        }
        else
        {
            pilihan = -1;
            break;
        }
        system("CLS");
        pilihan = selectMenu_1301204459();
    }
    cout << endl << "Anda Telah Keluar dari Program" << endl;
    cout << "Tekan Enter Untuk Exit";

    system("pause > nul");
    system("CLS");
    return 0;
}
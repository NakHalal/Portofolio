#include "menu.h"

int main()
{
    int NUM = 0, pilihan = 0, x;

    pilihan = selectMenu();
    while(pilihan != 0)
    {
        switch (pilihan)
        {
        case 1:
            cout << "Masukkan angka: ";
            cin >> x;
            inputAngka(NUM, x);
            break;
        case 2:
            cout << "Masukkan angka: ";
            cin >> x;
            tambah(NUM, x);
            break;
        case 3:
            printHasil(NUM);
            break;
        default:
            pilihan = -1;
            break;
        }
        system("CLS");
        pilihan = selectMenu();
    }
    cout << "BYE BYE" << endl;

    system("pause")
    return 0;
}
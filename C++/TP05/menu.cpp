#include "menu.h"

int selectMenu_1301204459()
{
    cout << "=_=_=_=_=_=_ Menu _=_=_=_=_=_=" << endl; 
    cout << "| 1. Menambahkan N Data Baru |" << endl;
    cout << "| 2. Menampilkan Semua Data  |" << endl;
    cout << "| 3. Hitung Jumlah           |" << endl;
    cout << "| 0. Exit                    |" << endl;
    cout << "=_=_=_=_=_=_  <3  _=_=_=_=_=_=" << endl;
    cout << endl << "Masukkan Menu: ";

    int input = 0;
    cin >> input;

    return input;
}
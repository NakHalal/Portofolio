#include "menu.h"

void inputAngka(int &NUM, int x)
{
    NUM = x;
}

void tambah(int &NUM, int x)
{
    NUM = NUM + x;
}

void printHasil(int NUM)
{
    cout << "Nilai saat ini: " << NUM << endl << endl;
    cout << "Tekan Enter untuk kembali ke Menu";
    system("pause >nul");
    // Sleep(3000);
    // usleep(3 * 1000000);
}

int selectMenu()
{
    cout << "==== MENU ====" << endl; 
    cout << "1. Input Angka Awal" << endl;
    cout << "2. Tambah" << endl;
    cout << "3. Print Hasil" << endl;
    cout << "0. Exit" << endl;
    cout << "Pilihan Menu: " << endl;

    int input = 0;
    cin >> input;

    return input;
}
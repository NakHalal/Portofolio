#include "menu.h"

string select_menu_1301204459()
{
    cout << "=================== Menu ===================" << endl; 
    cout << "| 1. Tambah Data Pegawai                   |" << endl; 
    cout << "| 2. Tampilkan Data Pegawai                |" << endl; 
    cout << "| 3. Cari Data Pegawai berdasarkan NIP     |" << endl; 
    cout << "| 4. Hapus Data Berdasarkan NIP            |" << endl; 
    cout << "| 5. Jumlah Pegawai Saat Ini               |" << endl; 
    cout << "| 6. Rata-Rata Penghasilan Pegawai         |" << endl; 
    cout << "| 7. Nama Pegawai dengan Gaji Tertinggi    |" << endl; 
    cout << "| 0. Selesai                               |" << endl; 
    cout << "==================== <3 ====================" << endl; 
    cout << endl << "Masukkan Menu: ";

    string input = "";
    cin >> input;
    cout << endl;

    return input;
}

void pause_1301204459()
{
    cout << endl;
    cout << "Tekan Enter Untuk Kembali Ke Menu";
    system("pause > nil");
    system("CLS");
}
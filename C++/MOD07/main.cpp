#include "ADT.h"

int main()
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    // Membuat List kosong
    listSingle L;
    create_list_1301204459(L);

    // Meminta data ke user sebanyak 10.
    // Lalu data yang diberikan user akan dimasukkan ke List
    // menggunakan insert yang sudah Anda buat
    int N = 10; // Tanggal 06 November 2021
    add_N_data_1301204459(L, N);
    cout << endl;

    // Menampilkan data yang sudah diinput tadi dengan procedure show
    cout << "Isi List Saat Ini: ";
    show_1301204459(L);
    cout << endl;

    // Memanggil fungsi procedure yang Anda buat pada tahapan ke-4
    // (cara pemanggilanbebas). Jika bentuknya fungsi maka return value 
    // dari fungsi tsb ditampilkan ke layar
    cout << "Jumlah Huruf A di List: ";
    cout << countX_1301204459(L, 'A') << endl;
    cout << "Jumlah Huruf I di List: ";
    cout << countX_1301204459(L, 'I') << endl;
    cout << "Jumlah Huruf U di List: ";
    cout << countX_1301204459(L, 'U') << endl;
    cout << "Jumlah Huruf E di List: ";
    cout << countX_1301204459(L, 'E') << endl;
    cout << "Jumlah Huruf O di List: ";
    cout << countX_1301204459(L, 'O') << endl;

    // Menghapus N data terbelakang.
    // N sesuai digit akhir NIM Anda.
    // Gunakan proceduredelete yang sudah Anda buat
    adrSingle temp;
    int O = 9; // Digit NIM Terakhir -> 1301204459
    delete_from_behind_1301204459(L, O);

    // Tampilkan list yang setelah Anda hapus datanya
    // dengan procedure show
    cout << endl << "Isi List Saat Ini: ";
    show_1301204459(L);

    cout << endl << "Tekan Enter Untuk Exit Program";
    system("pause > nul");
    system("CLS");
    return 0;
}
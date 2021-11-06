#include "mahasiswa.h"

void inputData_1301204459(mahasiswa *M) {
    int i = 0;

    cout << "Tuliskan NIM: ";
    cin >> M->NIM;

    while (i < Max)
    {
        cout << "Nilai " << i+1 << ": ";
        cin >> M->Nilai[i];
        i++;
    }
}

float mean_1301204459(mahasiswa M) {
    int i = 0;
    float tot;
    while (i < Max)
    {
        tot = tot + M.Nilai[i];
        i++;
    }
    return (tot/5);
}

void showData_1301204459(mahasiswa M) {
    cout << endl << "Data Mahasiswa: " << endl;
    cout << "NIM: " << M.NIM << endl;
    cout << "Nilai: " << M.Nilai[0] << " " << M.Nilai[1] <<  " " << M.Nilai[2] <<  " " << M.Nilai[3] <<  " " << M.Nilai[4] << endl;
    // cout << "Dengan Rata Rata Nilai: " << mean(M) << endl;  
}
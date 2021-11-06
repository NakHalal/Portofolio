#include "mahasiswa.h"

int main()
{
    mahasiswa x;
    
    inputData_1301204459(&x);
    showData_1301204459(x);
    
    cout << "Dengan Rata-Rata Nilai: " << mean_1301204459(x) << endl;

    system("pause");
}
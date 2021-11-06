#include <iostream>
#include <cstdlib>

using namespace std;

const int Max = 5;

struct mahasiswa{
    string NIM;
    float Nilai[Max];
};

void inputData_1301204459(mahasiswa *M);
float mean_1301204459(mahasiswa M);
void showData_1301204459(mahasiswa M);
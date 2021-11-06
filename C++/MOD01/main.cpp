#include <iostream>

using namespace std;

const int nMax = 10;

struct Himpunan{
    int anggota[nMax];
    int panjang;
};

bool anggotaHimpunan(Himpunan himp, int bil){
    bool found = false;
    int i = 0;
    while (i <= himp.panjang && !found) {
        found = bil == himp.anggota[i];
        i++;
    }
    return found;
}

void inputAnggotaHimpunan(Himpunan &himp) {
    int bilangan;
    himp.panjang = -1;
    cin >> bilangan;
    while (himp.panjang < nMax -1 && !anggotaHimpunan(himp, bilangan)) {
        himp.panjang++;
        himp.anggota[himp.panjang] = bilangan;
        cin >> bilangan;
    }
}

Himpunan irisan(Himpunan himp1, Himpunan himp2) {
    Himpunan intersect;
    intersect.panjang = -1;
    for (int i = 0; i <= himp1.panjang; i++) {
        for (int j = 0; j <= himp2.panjang; j++) {
            if (himp1.anggota[i] == himp2.anggota[j]) {
                intersect.panjang++;
                intersect.anggota[intersect.panjang] = himp1.anggota[i];
            }
        }
    }
    return intersect;
}

void printHimp(Himpunan himp) {
    int i = 0;
    while (i <= himp.panjang) {
        cout << himp.anggota[i] << " ";
        i++;
    }
    cout << endl;
}

int main()
{
    Himpunan set1;
    Himpunan set2;
    Himpunan set3;

    cout << "Anggota Himpunan 1: ";
    inputAnggotaHimpunan(set1);

    cout << "Anggota Himpunan 2: ";
    inputAnggotaHimpunan(set2);

    set3 = irisan(set1, set2);

    printHimp(set1);
    printHimp(set2);
    printHimp(set3);

    return 0;
}

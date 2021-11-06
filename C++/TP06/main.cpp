#include "SLL.h"
#include "menu.h"

int main()
{
    List L;
    adr P, temp;
    infotype Mhs;

    createList(L);

    Mhs = newMahasiswa("A", 1, 1);
    P = newElement(Mhs);
    insertLast(L, P);

    Mhs = newMahasiswa("B", 2, 2);
    P = newElement(Mhs);
    insertLast(L, P);

    Mhs = newMahasiswa("C", 3, 3);
    P = newElement(Mhs);
    insertLast(L, P);

    loopThis(L);

    cout << "Anda Telah Keluar dari Program" << endl;
    cout << "Tekan Enter Untuk Exit";

    system("pause > nul");
    system("CLS");
    return 0;
}
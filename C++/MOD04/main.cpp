#include "mylist.h"

int main()
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    List L;
    adr P, temp;
    infotype Mhs;

    createList_1301204459(L);
    printList_1301204459(L);
    Mhs = newMahasiswa_1301204459("Alice", "1301190202", 3.5);
    P = newElement_1301204459(Mhs);
    insertFirst_1301204459(L, P);
    Mhs = newMahasiswa_1301204459("Bob", "1301190203", 4);
    P = newElement_1301204459(Mhs);
    insertFirst_1301204459(L, P);
    printList_1301204459(L);
    Mhs = newMahasiswa_1301204459("Chihaya", "1301190204", 3.6);
    P = newElement_1301204459(Mhs);
    insertLast_1301204459(L, P);
    Mhs = newMahasiswa_1301204459("Delta", "1301190205", 2.7);
    P = newElement_1301204459(Mhs);
    insertLast_1301204459(L, P);
    Mhs = newMahasiswa_1301204459("Euniche", "1301190201", 3.9);
    P = newElement_1301204459(Mhs);
    insertFirst_1301204459(L, P);
    printList_1301204459(L);
    deleteFirst_1301204459(L, temp);
    deleteLast_1301204459(L, temp);
    printList_1301204459(L);

    cout << "[Input Mahasiswa]" << endl;
    string t_nama, t_nim; float t_ipk;
    while(!(t_nama == "-" && t_nim == "-"))
    {
        cout << "Masukkan Nama: ";
        cin >> t_nama;
        cout << "Masukkan NIM: ";
        cin >> t_nim;
        cout << "Masukkan IPK: ";
        cin >> t_ipk;
        cout << endl;

        if(t_nama != "-" && t_nim != "-")
        {
        Mhs = newMahasiswa_1301204459(t_nama, t_nim, t_ipk);
        P = newElement_1301204459(Mhs);
        insertLast_1301204459(L, P);
        }
    }    
    printList_1301204459(L);

    cout << "[Info Terhapus (deleteLast)]" << endl;
    int i = 1;
    while(L.First != NULL)
    {
        cout << "[" << i << "]" << endl;
        deleteLast_1301204459(L, temp);
        cout << "Nama: " << temp->info.nama << endl;
        cout << "NIM : " << temp->info.nim << endl;
        cout << "IPK : " << temp->info.ipk << endl;
        i++;
    }
    cout << endl;
    printList_1301204459(L);
    
    system("pause");

    return 0;
}
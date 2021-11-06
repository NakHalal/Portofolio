#include "mylist.h"

void createList_1301204459(List &L)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    L.First = NULL;
}

infotype newMahasiswa_1301204459(string nama, string nim, float ipk)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    infotype mhs;
    mhs.nama = nama;
    mhs.nim = nim;
    mhs.ipk = ipk;
    return mhs;
}

adr newElement_1301204459(infotype dataBaru)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    adr P = new elmList;
    P->info = dataBaru;
    P->next = NULL;
    return P;
}

void insertFirst_1301204459(List &L, adr P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    if (L.First == NULL)
    {
        L.First = P;
    }
    else
    {
        P->next = L.First;
        L.First = P;
    }   
}

void deleteFirst_1301204459(List &L, adr &temp)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    temp = L.First;
    L.First = L.First->next;
}

void printList_1301204459(List L)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    adr P;
    int i;
    if(L.First == NULL)
    {
        cout << "List Kosong" << endl << endl;
    }
    else
    {
        i = 1;
        P = L.First;
        while (P != NULL)
        {
            cout << "[" << i << "]" << endl;
            cout << "Nama: " << P->info.nama << endl;
            cout << "NIM : " << P->info.nim << endl;
            cout << "IPK : " << P->info.ipk << endl;
            P = P->next;
            i++;
        }
        cout << "List Telah Selesai Ditampilkan!" << endl << endl;
    }
}

void insertLast_1301204459(List &L, adr P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    adr Q;
    adr R;
    if (L.First == NULL)
    {
        L.First = P;
    }
    else if(L.First->next == NULL)
    {
        L.First->next = P;
    }
    else
    {
        Q = L.First;
        R = L.First;
        while (Q->next != NULL)
        {
            Q = R->next;
            R = Q;
        }
        Q->next = P;
    }
}

void deleteLast_1301204459(List &L, adr &temp)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    adr Q;
    adr P;
    if (L.First == NULL)
    {
        P = NULL;
        cout << "List Kosong" << endl;
    }
    else if (L.First->next == NULL)
    {
        P = L.First;
        L.First = NULL;
    }
    else
    {
        Q = L.First;
        P = L.First;
        while (P->next != NULL)
        {
            Q = P;
            P = P->next;
        }
        Q->next = NULL;
    }
    temp = P;
}
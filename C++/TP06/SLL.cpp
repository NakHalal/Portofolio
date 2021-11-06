#include "SLL.h"

void createList(List &NH)
{
    NH.first = NULL;
    NH.last = NULL;
}

infotype newMahasiswa(string nama, int nim, float ipk)
{
    infotype mhs;
    mhs.nama = nama;
    mhs.nim = nim;
    mhs.ipk = ipk;
    return mhs;
}

adr newElement(infotype dataBaru)
{
    adr P = new ElmList;
    P->info = dataBaru;
    P->next = NULL;
    P->prev = NULL;
    return P;
}

void insertFirst(List &NH, adr P)
{
    if (NH.first != NULL && NH.last != NULL)
    {
        P->next = NH.first;
        NH.first->prev = P;
        NH.first = P;
    }
    else
    {
        NH.first = P;
        NH.last = P;
    }
}


void insertLast(List &NH, adr P)
{
    if (NH.first != NULL && NH.last != NULL)
    {
    P->prev = NH.last;
    NH.last->next = P;
    NH.last = P;
    }
    else
    {
        insertFirst(NH, P);
    }
}

void insertAfter(List &NH, adr P, adr prec)
{
    P->next = prec->next;
    P->prev = prec;
    prec->next->prev = P;
    prec->next = P;
}

void deleteFirst(List &NH, adr &temp)
{
    temp = NH.first;
    if (NH.first != NH.last)
    {
        NH.first = temp->next;
        temp->next = NULL;
        NH.first->prev = NULL;
    }
    else
    {
        NH.first = NULL;
        NH.last = NULL;
    }
}

void deleteLast(List &NH, adr &temp)
{
    if (NH.first == NULL && NH.last == NULL)
    {
        deleteFirst(NH, temp);
    }
    else
    {
        temp = NH.last;
        NH.last = NH.last->prev;
        temp->prev = NULL;
        NH.last->next = NULL;
    }
}

void deleteAfter(List &NH, adr prec, adr &temp)
{
    temp = prec->next;
    prec->next = temp->next;
    temp->next->prev = prec;
    temp->prev = NULL;
    temp->next = NULL;
}

void deleteBefore(List &NH, adr prec, adr &temp)
{
    temp = prec->prev;
    prec->prev = temp->prev;
    temp->prev->next = prec;
    temp->prev = NULL;
    temp->next = NULL;
}

void printListFromFirst(List NH)
{
    adr P;
    int i;
    if(NH.first == NULL && NH.last == NULL)
    {
        cout << "List Kosong" << endl;
    }
    else
    {
        i = 1;
        P = NH.first;
        while (P != NULL)
        {
            cout << "[" << i << "]" << endl;
            cout << "Nama: " << P->info.nama << endl;
            cout << "NIM : " << P->info.nim << endl;
            cout << "IPK : " << P->info.ipk << endl;
            cout << endl;
            P = P->next;
            i++;
        }
        cout << "List Telah Selesai Ditampilkan!" << endl;
    }
}

int countList(List NH)
{
    adr Q = NH.first;
    int A = 0;
    if(Q == NULL)
    {
        return A;
    }
    else
    {
        while(Q != NULL)
        {
            Q = Q->next;
            A++;
        }
        return A;
    }
}

void printListFromLast(List NH)
{
    adr P;
    int i = countList(NH);
    if(NH.first == NULL && NH.last == NULL)
    {
        cout << "List Kosong" << endl << endl;
    }
    else
    {
        P = NH.last;
        while (P != NULL)
        {
            cout << "[" << i << "]" << endl;
            cout << "Nama: " << P->info.nama << endl;
            cout << "NIM : " << P->info.nim << endl;
            cout << "IPK : " << P->info.ipk << endl;
            cout << endl;
            P = P->prev;
            i--;
        }
        cout << "List Telah Selesai Ditampilkan!" << endl;
    }
}

void add_N_data(List &NH)
{
    int N;
    infotype temp;
    adr P;
    cout << "Jumlah Data yang Akan Ditambahkan: ";
    cin >> N;

    while (N > 0)
    {
        cout << endl << "Masukkan Data Baru: " << endl;
        cout << "Nama: ";
        cin >> temp.nama;
        cout << "NIM : ";
        cin >> temp.nim;
        cout << "IPK : ";
        cin >> temp.ipk;
        
        P = newElement(temp);
        insertLast(NH, P);

        N--;
    }
}

adr searchAddressByName(List &NH, string nama)
{
    adr P, Q;
    Q = NULL;
    P = NH.first;

    while (P != NULL)
    {
        if (P->info.nama == nama)
        {
            Q = P;
            break;
        }
        P = P->next;
    }

    return Q;    
}

adr searchAddressByNIM(List &NH, int nim)
{
    adr P, Q;
    Q = NULL;
    P = NH.first;

    while (P != NULL)
    {
        if (P->info.nim == nim)
        {
            Q = P;
            break;
        }
        P = P->next;
    }

    return Q;    
}

adr searchAddressByIPK(List &NH, float ipk)
{
    adr P, Q;
    Q = NULL;
    P = NH.first;

    while (P != NULL)
    {
        if (P->info.ipk == ipk)
        {
            Q = P;
            break;
        }
        P = P->next;
    }

    return Q;    
}

void deleteThis(List &NH, adr prec, adr &temp)
{
    adr P = NH.first;
    adr Q = NULL;

    while (P != NULL)
    {
        if (P == prec)
        {
            Q = P;
            break;
        }
        P = P->next;
    }
    if (Q != NULL)
    {
        if (Q != NH.first && Q != NH.last)
        {
            Q->prev->next = Q->next;
            Q->next->prev = Q->prev;
            Q->next = NULL;
            Q->prev = NULL;
        }
        else if (Q == NH.first)
        {
            deleteFirst(NH, temp);
        }
        else if (Q == NH.last)
        {
            deleteLast(NH, temp);
        }
    }
}
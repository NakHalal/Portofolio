#include "ADT.h"

void create_list_1301204459(listSingle &L)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    L.First = NULL;
}

adrSingle alokasi_1301204459(infotype new_data)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adrSingle x = new elmtSingle;

    x->info = new_data;
    x->next = NULL;

    return x;
}

void show_1301204459(listSingle L)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adrSingle P = L.First;
    if (L.First != NULL)
    {
        while (P != NULL)
        {
            cout << P->info << " ";
            P = P->next;
        }
        cout << endl;
    }
    else
    {
        cout << "List Kosong" << endl;
    } 
}

void insert_first_1301204459(listSingle &L, adrSingle new_data)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    if (L.First == NULL)
    {
        L.First = new_data;
    }
    else
    {
        new_data->next = L.First;
        L.First = new_data;
    }   
}

void insert_last_1301204459(listSingle &L, adrSingle new_data)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adrSingle Q;
    adrSingle R;
    if (L.First == NULL)
    {
        L.First = new_data;
    }
    else if(L.First->next == NULL)
    {
        L.First->next = new_data;
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
        Q->next = new_data;
    }
}

void add_N_data_1301204459(listSingle &L, int &N)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    infotype temp;
    adrSingle P;
    cout << "Masukkan " << N << " Data Baru: " << endl;

    while (N > 0)
    {
        cin >> temp;
        
        P = alokasi_1301204459(temp);
        insert_last_1301204459(L, P);

        N--;
    }
}

void delete_first_1301204459(listSingle &L, adrSingle &temp)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    temp = L.First;
    L.First = L.First->next;

}

void delete_last_1301204459(listSingle &L, adrSingle &temp)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adrSingle Q;
    adrSingle P;
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

void delete_from_behind_1301204459(listSingle &L, int &x)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adrSingle temp;
    adrSingle P = L.First;
    while (L.First != NULL && P != NULL && x > 0)
    {
        delete_last_1301204459(L, temp);
        x--;
    }
}

int countX_1301204459(listSingle L, infotype x)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adrSingle P = L.First;
    int Q = 0;
    while (L.First != NULL && P != NULL)
    {
        if (P->info == x)
        {
            Q++;
        }
        P = P->next;
    }
    return Q;
}
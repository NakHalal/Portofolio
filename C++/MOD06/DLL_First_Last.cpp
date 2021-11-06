#include "DLL_First_Last.h"

void createList_1301204459(List &L)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    L.First = NULL;
    L.Last = NULL;
}

adr createElement_1301204459(infotype dataBaru)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adr P = new ElmtList;

    P->prev = NULL;
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

    if (L.First != NULL && L.Last != NULL)
    {
        P->next = L.First;
        L.First->prev = P;
        L.First = P;
    }
    else
    {
        L.First = P;
        L.Last = P;
    }
}

void insertLast_1301204459(List &L, adr P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    if (L.First == NULL)
    {
        L.First = P;
        L.Last = P;
    }
    else
    {
        L.Last->next = P;
        P->prev = L.Last;
        L.Last = P;
    }
}

void insertAfter_1301204459(adr prec, adr P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    P->next = prec->next;
    prec->next->prev = P;
    prec->next = P;
    P->prev = prec;
}

void insertAscending_1301204459(List &L, infotype dataBaru)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adr P = createElement_1301204459(dataBaru);

    if (L.First == NULL)
    {
        insertFirst_1301204459(L, P);
    }
    else if (L.First->info >= P->info)
    {
        P->next = L.First;
        P->next->prev = P;
        L.First = P;
    }
    else
    {
        adr Q = L.First;

        while (Q->next != NULL && Q->next->info < P->info)
        {
            Q = Q->next;
        }
        
        P->next = Q->next;

        if (Q->next == NULL)
        {
            insertLast_1301204459(L, P);
        }
        else
        {
            if (Q->next != NULL)
            {
                P->next->prev = P;
            }
            Q->next = P;
            P->prev = Q;
        }
    }
}

void deleteFirst_1301204459(List &L, adr &P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    P = L.First;
    if (L.First->next == NULL)
    {
        L.First = NULL;
        L.Last = NULL;
    }
    else
    {
        L.First = L.First->next;
        L.First->prev = NULL;
        P->next = NULL;
    }
}

void deleteLast_1301204459(List &L, adr &P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    P = L.Last;
    if (L.First != NULL && L.Last != NULL)
    {
        L.Last = L.Last->prev;
        P->prev = NULL;
        L.Last->next = NULL;
    }
    else
    {
        L.First = P;
        L.Last = P;
    }
}

void deleteAfter_1301204459(adr prec, adr &P)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    P = prec->next;
    prec->next = P->next;
    P->next->prev = prec;
    P->next = NULL;
    P->prev = NULL;
}

void deleteElm_1301204459(List &L, infotype dataHapus)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    if (L.First != NULL && L.Last != NULL)
    {
        adr P = L.First;
        adr Q = L.First;
        adr temp;

        while (P->info != dataHapus)
        {
            Q = P;
            P = P->next;
        }

        if (P->info == dataHapus)
        {
            if (P == L.First)
            {
                deleteFirst_1301204459(L, temp);
            }
            else if (P == L.Last)
            {
                deleteLast_1301204459(L, temp);
            }
            else
            {
                deleteAfter_1301204459(Q, temp);
            }
        }
    }
}

void printList_1301204459(List L)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adr P = L.First;
    while (P != NULL)
    {
        cout << P->info << " ";
        P = P->next;
    }
    cout << endl;
}

bool findElement_1301204459(List L, infotype dataDicari)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adr P = L.First;
    while (P->info != dataDicari && P != L.Last)
    {
        P = P->next;
    }
    
    bool Q = false;
    if (P->info == dataDicari)
    {
        Q = true;
    }
    return Q;
}

int frequencyofElm_1301204459(List L, infotype dataDicari)
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
   
    int Count = 0;
    adr P = L.First;

    if (findElement_1301204459(L, dataDicari))
    {
        while (P != NULL)
        {
            if (P->info == dataDicari)
            {
                Count++;
            }
            P = P->next;
        }
    }
    return Count;
}
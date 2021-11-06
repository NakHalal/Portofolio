#include "SLL.h"

void createList_1301204459(List &NH)
{
    NH.first = NULL;
}

adr newElement_1301204459(infotype x)
{
    adr P = new element;
    P->info = x;
    P->next = NULL;
    return P;
}

void insertFirst_1301204459(List &NH, adr P)
{
    if (NH.first == NULL)
    {
        NH.first = P;
    }
    else
    {
        P->next = NH.first;
        NH.first = P;
    }   
}

void show_1301204459(List NH)
{
    adr P;
    if (NH.first != NULL)
    {
        P = NH.first;
        while (P != NULL)
        {
            cout << P->info << " ";
            P = P->next;
        }
        cout << endl;
        
    }
    else
    {
        cout << "Kosong" << endl;
    }
}

void deleteLast_1301204459(List &NH, adr &temp)
{
    adr Q;
    adr P;
    if (NH.first == NULL)
    {
        P = NULL;
        cout << "Kosong" << endl;
    }
    else if (NH.first->next == NULL)
    {
        P = NH.first;
        NH.first = NULL;
    }
    else
    {
        Q = NH.first;
        P = NH.first;
        while (P->next != NULL)
        {
            Q = P;
            P = P->next;
        }
        Q->next = NULL;
    }
    temp = P;
}

void insertLast_1301204459(List &NH, adr P)
{
    adr Q;
    adr R;
    if (NH.first == NULL)
    {
        NH.first = P;
    }
    else if (NH.first->next == NULL)
    {
        NH.first->next = P;
    }
    else
    {
        Q = NH.first;
        R = NH.first;
        while (Q->next != NULL)
        {
            Q = R->next;
            R = Q;
        }
        Q->next = P;
    }
}

void insertAfter_1301204459(List &NH, int X, adr P)
{
    adr Q = NH.first;
    adr R = NH.first;
    adr S;
    bool DOIT = true;
    if(X==0)
    {
        insertFirst_1301204459(NH, P);
    }
    else if(X==1)
    {
        S = NH.first->next;
        NH.first->next = P;
        P->next = S;
    }
    else
    {
        while (X > 1)
        {
            Q = R->next;
            R = Q;
            if(R->next == NULL)
            {
                cout << "List Tidak Mencukupi" << endl;
                DOIT = false;
                break;
            }
            S = Q->next;
            X--;
        }
        if(DOIT == true)
        {
            Q->next = P;
            P->next = S;
        }
    }
}

void deleteFirst_1301204459(List &NH, adr &temp)
{
    temp = NH.first;
    NH.first = NH.first->next;
}

void deleteAfter_1301204459(List &NH, int X, adr &temp)
{
    adr Q = NH.first;
    adr R = NH.first;
    adr S;
    bool DOIT = true;
    if(X==0)
    {
        deleteFirst_1301204459(NH, temp);
    }
    else if(X==1)
    {
        S = NH.first->next;
        NH.first->next = NH.first->next->next;
    }
    else
    {
        while (X > 1)
        {
            Q = R->next;
            R = Q;
            if(R->next == NULL)
            {
                cout << "List Tidak Mencukupi" << endl;
                DOIT = false;
                break;
            }
            S = Q->next->next;
            X--;
        }
        if(DOIT == true)
        {
            temp = Q->next;
            Q->next = S;
        }
    }
}

int countAll_1301204459(List NH)
{
    adr Q = NH.first;
    int A = 0;
    if(Q == NULL)
    {
        return A;
    }
    else
    {
        while(Q->next != NULL)
        {
            Q = Q->next;
            A++;
        }
        return A+1;
    }
}
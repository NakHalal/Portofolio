#include "SLL.h"

void createList_1301204459(List &NH)
{
    first(NH) = NULL;
}

adr newElement_1301204459(infotype x)
{
    adr P = new element;
    info(P) = x;
    next(P) = nil;
    return P;
}

void insertFirst_1301204459(List &NH, adr P)
{
    if (first(NH) == nil)
    {
        first(NH) = P;
    }
    else
    {
        next(P) = first(NH);
        first(NH) = P;
    }   
}

void show_1301204459(List NH)
{
    adr P;
    if (first(NH) != nil)
    {
        P = first(NH);
        while (P != nil)
        {
            cout << info(P) << " ";
            P = next(P);
        }
        cout << endl;
        
    }
    else
    {
        cout << "show -> List Kosong" << endl;
    }
}

adr deleteLast_1301204459(List &NH)
{
    adr Q;
    adr P;
    if (first(NH) == nil)
    {
        P = nil;
        cout << "List Kosong" << endl;
    }
    else if (next(first(NH)) == nil)
    {
        P = first(NH);
        first(NH) = nil;
    }
    else
    {
        Q = first(NH);
        P = first(NH);
        while (next(P) != nil)
        {
            Q = P;
            P = next(P);
        }
        next(Q) = nil;
    }
    return P;
}

void insertLast_1301204459(List &NH, adr P)
{
    adr Q;
    adr R;
    if (first(NH) == nil)
    {
        first(NH) = P;
    }
    else if (next(first(NH)) == nil)
    {
        next(first(NH)) = P;
    }
    else
    {
        Q = first(NH);
        R = first(NH);
        while (next(Q) != nil)
        {
            Q = next(R);
            R = Q;
        }
        next(Q) = P;
    }
}

void insertAfter_1301204459(List &NH, int X, adr P)
{
    adr Q = first(NH);
    adr R = first(NH);
    adr S;
    bool DOIT = true;
    if(X==0)
    {
        insertFirst_1301204459(NH, P);
    }
    else if(X==1)
    {
        S = next(first(NH));
        next(first(NH)) = P;
        next(P) = S;
    }
    else
    {
        while (X > 1)
        {
            Q = next(R);
            R = Q;
            if(next(R) == nil)
            {
                cout << "insertAfter -> List Tidak Mencukupi" << endl;
                DOIT = false;
                break;
            }
            S = next(Q);
            X--;
        }
        if(DOIT == true)
        {
            next(Q) = P;
            next(P) = S;
        }
    }
}

void deleteFirst_1301204459(List &NH)
{
    first(NH) = next(first(NH));
}

void deleteAfter_1301204459(List &NH, int X)
{
    adr Q = first(NH);
    adr R = first(NH);
    adr S;
    bool DOIT = true;
    if(X==0)
    {
        deleteFirst_1301204459(NH);
    }
    else if(X==1)
    {
        S = next(first(NH));
        next(first(NH)) = next(next(first(NH)));
    }
    else
    {
        while (X > 1)
        {
            Q = next(R);
            R = Q;
            if(next(R) == nil)
            {
                cout << "deleteAfter -> List Tidak Mencukupi" << endl;
                DOIT = false;
                break;
            }
            S = next(next(Q));
            X--;
        }
        if(DOIT == true)
        {
            next(Q) = S;
        }
    }
}
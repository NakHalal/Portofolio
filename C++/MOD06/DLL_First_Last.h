#ifndef DLL_First_Last_INCLUDED
#define DLL_First_Last_INCLUDED

#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <bits/stdc++.h>
using namespace std;

typedef int infotype;
typedef struct ElmtList *adr;

struct ElmtList
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    adr prev;
    infotype info;
    adr next;
};

struct List
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
   
    adr First;
    adr Last;
};

void createList_1301204459(List &L);
adr createElement_1301204459(infotype dataBaru);

void insertFirst_1301204459(List &L, adr P);
void insertLast_1301204459(List &L, adr P);
void insertAfter_1301204459(adr prec, adr P);
void insertAscending_1301204459(List &L, infotype dataBaru);

void deleteFirst_1301204459(List &L, adr &P);
void deleteLast_1301204459(List &L, adr &P);
void deleteAfter_1301204459(adr prec, adr &P);
void deleteElm_1301204459(List &L, infotype dataHapus);

void printList_1301204459(List L);

bool findElement_1301204459(List L, infotype dataDicari);
int frequencyofElm_1301204459(List L, infotype dataDicari);

#endif // DLL_First_Last_INCLUDED
#ifndef MYLIST_H_INCLUDED
#define MYLIST_H_INCLUDED

#include <iostream>
using namespace std;

struct mahasiswa
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    string nama;
    string nim;
    float ipk;
};

typedef mahasiswa infotype;
typedef struct elmList* adr;

struct List
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    adr First;
};

struct elmList
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    infotype info;
    adr next;
};

void createList_1301204459(List &L);
infotype newMahasiswa_1301204459(string nama, string nim, float ipk);
adr newElement_1301204459(infotype dataBaru);
void insertFirst_1301204459(List &L, adr P);
void insertLast_1301204459(List &L, adr P);
void deleteFirst_1301204459(List &L, adr &temp);
void deleteLast_1301204459(List &L, adr &temp);
void printList_1301204459(List L);

#endif // MYLIST_H_INCLUDED
#ifndef SLL_H_INCLUDED
#define SLL_H_INCLUDED

#include <iostream>
#include <stdlib.h>
using namespace std;

/*
#define info(P) (P)->info
#define next(P) (P)->next
#define first(NH) ((NH).first)
#define nil NULL
*/

struct mhs
{
    string nama;
    int nim;
    float ipk;
};

typedef mhs infotype;
typedef struct ElmList *adr;

struct ElmList
{
    adr prev;
    infotype info;
    adr next;
};

struct List
{
    adr first;
    adr last;
};

void createList(List &NH);
infotype newMahasiswa(string nama, int nim, float ipk);
adr newElement(infotype dataBaru);
void insertFirst(List &NH, adr P);
void insertLast(List &NH, adr P);
void insertAfter(List &NH, adr P, adr prec);
void deleteFirst(List &NH, adr &temp);
void deleteLast(List &NH, adr &temp);
void deleteAfter(List &NH, adr prec, adr &temp);
void deleteBefore(List &NH, adr prec, adr &temp);

void deleteThis(List &NH, adr prec, adr &temp);

adr searchAddressByName(List &NH, string nama);
adr searchAddressByNIM(List &NH, int nim);
adr searchAddressByIPK(List &NH, float ipk);

void printListFromFirst(List NH);
void printListFromLast(List NH);
int countList(List NH);

void add_N_data(List &NH);

#endif // SLL_H_INCLUDED
#ifndef SLL_H_INCLUDED
#define SLL_H_INCLUDED

#include "menu.h"
#include <iostream>
#include <stdlib.h>
using namespace std;

/*
#define info(P) (P)->info
#define next(P) (P)->next
#define first(NH) ((NH).first)
#define nil NULL
*/

typedef string infotype;
typedef struct element *adr;

struct element
{
    infotype info;
    adr next;
};

struct List
{
    adr first;
};

void createList_1301204459(List &NH);
adr newElement_1301204459(infotype x);
void insertFirst_1301204459(List &NH, adr P);
void show_1301204459(List NH);
void deleteLast_1301204459(List &NH, adr &temp);

void insertLast_1301204459(List &NH, adr P);
void insertAfter_1301204459(List &NH, int X, adr P);
void deleteFirst_1301204459(List &NH, adr &temp);
void deleteAfter_1301204459(List &NH, int X, adr &temp);

int countAll_1301204459(List NH);

#endif // SLL_H_INCLUDED
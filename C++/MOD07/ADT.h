#ifndef ADT_H_INCLUDED
#define ADT_H_INCLUDED

#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <bits/stdc++.h>
using namespace std;

typedef char infotype;
typedef struct elmtSingle *adrSingle;

struct elmtSingle
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    infotype info;
    adrSingle next;
};

struct listSingle
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
   
    adrSingle First;
};

void create_list_1301204459(listSingle &L);
adrSingle alokasi_1301204459(infotype new_data);
void show_1301204459(listSingle L);
void insert_first_1301204459(listSingle &L, adrSingle new_data);
void insert_last_1301204459(listSingle &L, adrSingle new_data);
void delete_first_1301204459(listSingle &L, adrSingle &temp);
void delete_last_1301204459(listSingle &L, adrSingle &temp);
void add_N_data_1301204459(listSingle &L, int &N);
int countX_1301204459(listSingle L, infotype x);
void delete_from_behind_1301204459(listSingle &L, int &x);

#endif // ADT_H_INCLUDED
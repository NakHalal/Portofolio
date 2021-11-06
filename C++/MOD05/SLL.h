#ifndef SLL_H_INCLUDED
#define SLL_H_INCLUDED

#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <bits/stdc++.h>
using namespace std;

struct pegawai
{
    string nama, NIP;
    int gaji;
};

typedef pegawai infotype;
typedef struct ElmtPeg *adr;

struct ElmtPeg
{
    infotype info;
    adr next;
};

struct List
{
    adr first;
};

void create_list_1301204459(List &L);
void insert_last_1301204459(List &L, adr P);
void delete_first_1301204459(List &L, adr &P);
void delete_last_1301204459(List &L, adr &P);
void delete_after_1301204459(List &L, adr prec, adr &P);
void new_element_1301204459(infotype peg, adr &P);
void add_N_data_1301204459(List &ListPeg);
void show_all_data_1301204459(List ListPeg);
adr search_by_NIP_1301204459(List ListPeg, string NIP);
void delete_Data_1301204459(List &ListPeg, string NIP);
int jumlah_pegawai_1301204459(List ListPeg);
int total_salary_1301204459(List ListPeg);
adr highest_salary_1301204459(List ListPeg);
string thousandSeparatorInt_1301204459(int n);

#endif // SLL_H_INCLUDED
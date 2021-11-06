#include <iostream>
#include <cstdlib>

using namespace std;

const int nMax = 50;

struct catalog
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    int data[nMax];
    int max;
    int num;
};

void add_data_1301204459(catalog &C, int x);
void view_data_1301204459(catalog C);
int search_data_1301204459(catalog C, int x);
void reversed_view_1301204459(catalog C);
void delete_data_1301204459(catalog &C);
#include "catalog.h"

void add_data_1301204459(catalog &C, int x) {
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    if(C.num < C.max) {
        C.num++;
        C.data[C.num] = x;
    }
}

int search_data_1301204459(catalog C, int x) {
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    int i = 0;
    while(i < C.max) {
        if(C.data[i] == x) {
            return i;
        }
        i++;
    }
    return -1;
}

void view_data_1301204459(catalog C) {
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    int i = 0;
    while(i <= C.num) {
        cout << C.data[i] << " ";
        i++;
    }
    cout << endl;
}

void reversed_view_1301204459(catalog C) {
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    int i = C.num;
    while(i >= 0) {
        cout << C.data[i] << " ";
        i--;
    }
    cout << endl;
}

void delete_data_1301204459(catalog &C) {
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */
    C.num--;
}

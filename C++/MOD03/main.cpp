#include "catalog.h"

int main()
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    //Inisiasi Varabel
    catalog storage;
    storage.max = 8;
    storage.num = -1;

    //Menambahkan data & Output
    add_data_1301204459(storage, 6);
    view_data_1301204459(storage);
    add_data_1301204459(storage, 4);
    view_data_1301204459(storage);
    add_data_1301204459(storage, 8);
    view_data_1301204459(storage);
    add_data_1301204459(storage, 2);
    view_data_1301204459(storage);
    cout<<endl;
    
    //mencari index
    int i;
    i = search_data_1301204459(storage, 8);
    cout<<i<<endl;
    i = search_data_1301204459(storage, 5);
    cout<<i<<endl;

    cout << endl;
    reversed_view_1301204459(storage);
    add_data_1301204459(storage, 5);
    reversed_view_1301204459(storage);
    cout << endl;

    view_data_1301204459(storage);
    delete_data_1301204459(storage);
    view_data_1301204459(storage);

    system("pause");

    return 0;
}
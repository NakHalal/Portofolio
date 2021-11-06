#include "DLL_First_Last.h"

int main()
{
    /*
    Name : Haidaruddin Muhammad Ramdhan
    NIM : 1301204459
    */

    List L;
    createList_1301204459(L);
    printList_1301204459(L);

    insertAscending_1301204459(L, 25);
    printList_1301204459(L);
    insertAscending_1301204459(L, 10);
    printList_1301204459(L);
    insertAscending_1301204459(L, 32);
    printList_1301204459(L);
    insertAscending_1301204459(L, 3);
    printList_1301204459(L);

    deleteElm_1301204459(L, 32);
    printList_1301204459(L);
    deleteElm_1301204459(L, 3);
    printList_1301204459(L);
    deleteElm_1301204459(L, 10);
    printList_1301204459(L);
    deleteElm_1301204459(L, 25);
    printList_1301204459(L);

    insertAscending_1301204459(L, 25);
    printList_1301204459(L);
    insertAscending_1301204459(L, 10);
    printList_1301204459(L);
    insertAscending_1301204459(L, 10);
    printList_1301204459(L);
    insertAscending_1301204459(L, 25);
    printList_1301204459(L);
    insertAscending_1301204459(L, 25);
    printList_1301204459(L);

    cout << endl;
    cout << boolalpha << findElement_1301204459(L, 10) << endl;
    cout << frequencyofElm_1301204459(L, 10) << endl;
    cout << frequencyofElm_1301204459(L, 25) << endl;
    cout << frequencyofElm_1301204459(L, 2) << endl;

    system("pause > nul");
    system("CLS");
    return 0;
}
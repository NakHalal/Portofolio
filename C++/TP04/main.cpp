#include "SLL.h"

using namespace std;

int main()
{
    // CreateList [Start]
    cout << "           [Start] CreateList [Start]" << endl;

    List NH;
    cout << "first(NH) sebelum createList: " << first(NH) << endl;

    createList_1301204459(NH);
    cout << "first(NH) setelah createList: " << first(NH) << endl;
    
    cout << "           [End] CreateList [End]" << endl << endl;
    // CreateList [End]

    // NewElement [Start]
    cout << "           [Start] NewElement [Start]" << endl;

    adr P;
    P = newElement_1301204459("YXGK");
    cout << "Info(P): " << info(P) << endl;
    cout << "next(P): " << next(P) << endl;
    
    cout << "           [End] NewElement [End]" << endl << endl;
    // NewElement [End]

    // InsertFirst [Start]
    cout << "           [Start] InsertFirst [Start]" << endl;

    cout << "first(NH) sebelum insertFirst: " << first(NH) << endl;
    insertFirst_1301204459(NH, P);

    cout << "first(NH) setelah insertFirst: " << first(NH) << endl;
    cout << "info first(NH): " << info(first(NH)) << endl;

    P = newElement_1301204459("YNTKTS");
    insertFirst_1301204459(NH, P);
    cout << "info first(NH): " << info(first(NH)) << endl;
    
    cout << "           [End] InsertFirst [End]" << endl << endl;
    // InsertFirst [End]

    // Show [Start]
    cout << "           [Start] Show [Start]" << endl;
    
    show_1301204459(NH);

    P = newElement_1301204459("YTBJTS");
    insertFirst_1301204459(NH, P);
    show_1301204459(NH);
    
    cout << "           [End] Show [End]" << endl << endl;
    // Show [End]

    // DeleteLast [Start]
    cout << "           [Start] DeleteLast [Start]" << endl;

    P = deleteLast_1301204459(NH);
    show_1301204459(NH);
    cout << info(P) << endl << endl;

    P = deleteLast_1301204459(NH);
    show_1301204459(NH);
    cout << info(P) << endl << endl;

    P = deleteLast_1301204459(NH);
    show_1301204459(NH);
    cout << info(P) << endl;

    cout << "           [End] DeleteLast [End]" << endl << endl;
    // DeleteLast [End]

    // InsertLast [Start]
    cout << "           [Start] InsertLast [Start]" << endl;

    P = newElement_1301204459("TES_01");
    insertLast_1301204459(NH, P);
    show_1301204459(NH);

    P = newElement_1301204459("TES_02");
    insertLast_1301204459(NH, P);
    show_1301204459(NH);

    P = newElement_1301204459("TES_03");
    insertLast_1301204459(NH, P);
    show_1301204459(NH);

    P = newElement_1301204459("TES_04");
    insertLast_1301204459(NH, P);
    show_1301204459(NH);

    P = newElement_1301204459("TES_05");
    insertLast_1301204459(NH, P);
    show_1301204459(NH);

    cout << "           [End] InsertLast [End]" << endl << endl;
    // InsertLast [End]

    // InsertAfter [Start]
    cout << "           [Start] InsertAfter [Start]" << endl;

    P = newElement_1301204459("P_01");
    insertAfter_1301204459(NH, 2, P);
    show_1301204459(NH);

    P = newElement_1301204459("P_02");
    insertAfter_1301204459(NH, 3, P);
    show_1301204459(NH);

    P = newElement_1301204459("P_03");
    insertAfter_1301204459(NH, 4, P);
    show_1301204459(NH);

    P = newElement_1301204459("P_99");
    insertAfter_1301204459(NH, 99, P);
    show_1301204459(NH);
    
    cout << "           [End] InsertAfter [End]" << endl << endl;
    // InsertAfter [End]

    // DeleteFirst [Start]
    cout << "           [Start] DeleteFirst [Start]" << endl;

    deleteFirst_1301204459(NH);
    show_1301204459(NH);

    deleteFirst_1301204459(NH);
    show_1301204459(NH);

    deleteFirst_1301204459(NH);
    show_1301204459(NH);
    
    cout << "           [End] DeleteFirst [End]" << endl << endl;
    // DeleteFirst [End]
    
    // DeleteAfter [Start]
    cout << "           [Start] DeleteAfter [Start]" << endl;

    deleteAfter_1301204459(NH, 3);
    show_1301204459(NH);

    deleteAfter_1301204459(NH, 2);
    show_1301204459(NH);

    deleteAfter_1301204459(NH, 1);
    show_1301204459(NH);

    deleteAfter_1301204459(NH, 99);
    show_1301204459(NH);

    cout << "           [End] DeleteAfter [End]" << endl << endl;
    // DeleteAfter [End]

    system("pause");

    return 0;
}

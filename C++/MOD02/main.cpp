#include "main.h"

struct mhs{
    string nama, NIM;
    float ipk;
    int semester, kode_unik;
};

struct prod{
    int AoC, CC, MH = 0;
};

void inputData_1301204459(mhs *DATA, int JDat, prod &prodigy)
{
    int n = 0;
    string BAK;
    JDat;
    while (n <= JDat) {
        cout << "Data ke-" << n+1 << endl;

        cout << "Nama: ";
        cin >> DATA[n].nama;

        cout << "NIM: ";
        cin >> DATA[n].NIM;

        BAK = DATA[n].NIM.substr(1,1);

        if (BAK == "1")
        {
            cout << "Prodi Anda adalah Art of Coffe" << endl;
            prodigy.AoC++;
        } else if (BAK == "2")
        {
            cout << "Prodi Anda adalah Creative Content" << endl;
            prodigy.CC++;
        } else if (BAK == "3")
        {
            cout << "Prodi Anda adalah Mental Health" << endl;
            prodigy.MH++;
        }
        
        cout << "IPK: ";
        cin >> DATA[n].ipk;

        cout << "Semester: ";
        cin >> DATA[n].semester;

        if (DATA[n].ipk > 3.5 && DATA[n].semester <= 8)
        {
            cout << "CUMLAUDE" << endl;
        }
        
        cout << "Kode Unik: ";
        cin >> DATA[n].kode_unik;

        int i, m=0, flag=0;  
        m=DATA[n].kode_unik/2;  
        for(i = 2; i <= m; i++)  
        {  
            if(DATA[n].kode_unik % i == 0)  
            {  
                //cout<<"Number is not Prime."<<endl;  
                flag=1;  
                break;  
            }            
        } 
        if (DATA[n].kode_unik == 1 || DATA[n].kode_unik == 0)
        {
            flag=1;
        }
        if (flag==0)  
        {
            cout << "MAHASISWA BERPRESTASI" << endl << endl; 
        } else
        {
            cout << endl; 
        }

        n++;
    }
}

int FindIt_1301204459(mhs *DATA, int n)
{
    int i;
    int MI = 0;
    n++;
    
    float max = DATA[0].ipk;

    for (i = 1; i < n; i++)
    {
        if (DATA[i].ipk > max)
        {
            MI = i;
            max = DATA[i].ipk;
        }
    }
    return MI;
}

int main()
{
    prod prodigy;

    cout << "Jumlah Data: ";
    int JDat;
    cin >> JDat;
    const int JCDat = JDat;
    --JDat;
    mhs DATA[JCDat];

    cout << endl;
    inputData_1301204459(DATA, JDat, prodigy);
    
    cout << "_____INPUT DATA SELESAI_____" << endl << endl;

    int IndexMaxIPK = FindIt_1301204459(DATA, JDat);

    cout << "IPK terbesar didapatkan oleh " << DATA[IndexMaxIPK].nama << endl;

    cout << "Program Studi Art of Coffee : " << prodigy.AoC << endl;
    cout << "Program Studi Creative Content : " << prodigy.CC << endl;
    cout << "Program Studi Mental Health : " << prodigy.MH << endl;

    system("pause");

    return 0;
}

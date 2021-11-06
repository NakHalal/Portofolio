#include "SLL.h"

void create_list_1301204459(List &L)
{
    L.first = NULL;
}

void insert_last_1301204459(List &L, adr P)
{
    if (L.first == NULL)
    {
        L.first=P;
    }
    else
    {
        adr addressBerjalan = L.first;
        while (addressBerjalan->next != NULL) {
            addressBerjalan = addressBerjalan->next;
        }
        addressBerjalan->next = P;
    }
}

void delete_first_1301204459(List &L, adr &P)
{
    P = L.first;
    if (L.first->next == NULL)
    {
        L.first = NULL;
    }
    else
    {
        L.first = L.first->next;
    }
    P->next = NULL;
}

void delete_last_1301204459(List &L, adr &P)
{
    adr q = L.first;
    while (q->next->next != NULL)
    {
        q = q->next;
    }
    P = q->next;
    q->next = NULL;
}

void delete_after_1301204459(List &L, adr Prec, adr &P)
{
    P = Prec->next;
    Prec->next = P->next;
    P->next = NULL;
}

infotype new_mahasiswa_1301204459(string nama, string NIP, int gaji)
{
    infotype pegawai;
    pegawai.nama = nama;
    pegawai.NIP = NIP;
    pegawai.gaji = gaji;
    return pegawai;
}

void new_element_1301204459(infotype pegawaiBaru, adr &P)
{
    adr X = new ElmtPeg;
    X->info = pegawaiBaru;
    X->next = NULL;
    P = X;
}

void add_N_data_1301204459(List &ListPeg)
{
    int N;
    infotype temp;
    cout << "Jumlah Data yang Akan Ditambahkan: ";
    cin >> N;

    while (N > 0)
    {
        cout << endl << "Masukkan Data Baru: " << endl;
        cout << "Nama Pegawai: ";
        cin >> temp.nama;
        cout << "NIP         : ";
        cin >> temp.NIP;
        cout << "Gaji        : ";
        cin >> temp.gaji;
        
        adr P;
        new_element_1301204459(temp, P);
        insert_last_1301204459(ListPeg, P);

        N--;
    }
}

void show_all_data_1301204459(List ListPeg)
{
    adr P;
    int i;
    if(ListPeg.first == NULL)
    {
        cout << "Tidak Ada Data Pegawai" << endl;
    }
    else
    {
        i = 1;
        P = ListPeg.first;
        while (P != NULL)
        {
            int N = P->info.gaji;
            string s = thousandSeparatorInt_1301204459(N);
            cout << "[[ Data ke-" << i << " ]]" << endl;
            cout << "Nama Pegawai: " << P->info.nama << endl;
            cout << "NIP         : " << P->info.NIP << endl;
            cout << "Gaji        : Rp" << s << ",00" << endl;
            cout << endl;
            P = P->next;
            i++;
        }
        cout << "Data Semua Pegawai Telah Selesai Ditampilkan!" << endl;
    }
}

adr search_by_NIP_1301204459(List ListPeg, string NIP)
{
    adr X, temp;
    bool FOUND = false;

    temp = ListPeg.first;
    if (temp != NULL)
    {
        if (temp->info.NIP == NIP)
        {
            FOUND = true;
            X = temp;
        }
        while ((temp->info.NIP != NIP && temp->next != NULL) && FOUND == false)
        {
            if (temp->next != NULL)
            {
                temp = temp->next;
            }
            if (temp->info.NIP == NIP)
            {
                FOUND = true;
                X = temp;
            }
        }
        
        if (FOUND == true)
        {
            return X;
        }
        else
        {
            return NULL;
        }
    }
    else
    {
        return NULL;
    }
}

void delete_Data_1301204459(List &ListPeg, string NIP)
{
    adr DeleteThis = search_by_NIP_1301204459(ListPeg, NIP);
    adr X = ListPeg.first;
    adr Y = ListPeg.first;

    adr P;
    if (DeleteThis == NULL)
    {
        cout << "NIP Tidak Ditemukan" << endl;
    }
    else
    {
        if (X == DeleteThis)
        {
            delete_first_1301204459(ListPeg, P);
        }
        else
        {
            while (X != DeleteThis)
            {
                Y = X;
                X = X->next;
            }
            if (X == DeleteThis)
            {
                delete_after_1301204459(ListPeg, Y, P);
            }
        }
    }
}

int jumlah_pegawai_1301204459(List ListPeg)
{
    int X = 0;
    adr P = ListPeg.first;

    while (P != NULL)
    {
        X++;
        P = P->next;
    }

    return X;
}

int total_salary_1301204459(List ListPeg)
{
    int X = 0;
    adr P = ListPeg.first;

    while (P != NULL)
    {
        X = X + P->info.gaji;
        P = P->next;
    }

    return X;
}

adr highest_salary_1301204459(List ListPeg)
{
    adr Q = NULL;
    if(ListPeg.first != NULL)
    {
        int X = 0;
        adr P = ListPeg.first;
        Q = ListPeg.first;

        if (P != NULL)
        {
            X = P->info.gaji;
            Q = P;
        }
        while (P != NULL && P->next != NULL)
        {
            P = P->next;
            if (P->info.gaji > X)
            {
                X = P->info.gaji;
                Q = P;
            };
        }
    }
    return Q;
}

string thousandSeparatorInt_1301204459(int n)
{
    string ans = "";
    string num = to_string(n);
  
    int count = 0;
  
    for (int i = num.size() - 1; i >= 0; i--)
    {
        count++;
        ans.push_back(num[i]);
  
        if (count == 3)
        {
            ans.push_back('.');
            count = 0;
        }
    }

    reverse(ans.begin(), ans.end());
  
    if (ans.size() % 4 == 0)
    {
        ans.erase(ans.begin());
    }
  
    return ans;
}
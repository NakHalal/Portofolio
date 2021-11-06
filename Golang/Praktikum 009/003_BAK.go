package main

import "fmt"

/*
procedure tambahBuku(in/out kardus: TabBuku, atas:integer)
{IS. Terdefinisi sebuah array kardus, di mana buku paling luar berada pada
indek atas
FS. nilai atas bertambah 1, dan sebuah buku ditambahkan pada indek atas, data
buku berasal dari input user}
procedure ambilBuku(in/out kardus: TabBuku, atas:integer, ambil:buku)
{IS. Terdefinisi sebuah array kardus, di mana buku paling luar berada pada
indek atas
FS. Ambil berisi buku paling atas/luar, nilai atas berkurang satu}
procedure findBook(in/out kardus: TabBuku, atas:integer in X:string)
{IS.Terdefinisi sebuah array kardus, di mana buku paling luar berada pada indek atas, X berisi judul sebuah buku
FS. Mencari buku dengan judul X, menampilkan semua judul buku yang dikeluarkan dari kardus, dan menampilkan
*/

type Buku struct {
	judul   string
	penulis string
	tahun   int
}

func findBook(TabBuku [5]Buku, n string, Z *int) int {
	var found bool = false
	for !found && *Z < 5 {
		found = n == TabBuku[*Z].judul
		if found {
			break
		}
		*Z++
	}
	if found {
		return *Z
	} else {
		return -1
	}
}

func tambahBuku(TabBuku *[5]Buku, Kardus *[5]Buku, Outermost *int) {
	var X string
	var Z int
	var i int = 0
	for X != "." {
		fmt.Print("Masukkan Judul Buku (Stop dengan \".\"): ")
		fmt.Scan(&X)
		Z = 0
		if findBook(*TabBuku, X, &Z) != -1 {
			Kardus[i] = TabBuku[Z]
			fmt.Println("Added!")
			*Outermost = i
			i++
		}
	}
}

func ambilBuku(TabBuku *[5]Buku, Kardus *[5]Buku, Outermost *int) {
	//fmt.Print(Kardus[*Outermost])
	Kardus[*Outermost] = Buku{"", "", 0}
	*Outermost--
}

func cariBuku(X string, TabBuku *[5]Buku, Kardus *[5]Buku, Outermost *int) {
	found := false
	for !found {
		if X == Kardus[*Outermost].judul {
			found = true
			fmt.Println("KETEMU")
			break
		} else if !found && *Outermost == 0 {
			fmt.Println(Kardus[*Outermost].judul)
			fmt.Println("TIDAK KETEMU")
			break
		} else {
			fmt.Println(Kardus[*Outermost].judul)
			ambilBuku(TabBuku, Kardus, Outermost)
		}
	}
}

func main() {
	var s1, s2, s3, s4, s5 Buku
	s1.judul, s1.penulis, s1.tahun = "A", "Adam", 2001
	s2.judul, s2.penulis, s2.tahun = "C", "Chaplin", 1997
	s3.judul, s3.penulis, s3.tahun = "ZZ", "Zeus", 2012
	s4.judul, s4.penulis, s4.tahun = "K", "Kendall", 1985
	s5.judul, s5.penulis, s5.tahun = "X", "Xavier", 1970
	var TabBuku = [5]Buku{s1, s2, s3, s4, s5}
	/*
		1. Buatlah sebuah kardus kosong, di mana atas bernilai -1
	*/
	var Kardus [5]Buku
	var Outermost = -1
	//fmt.Print(TabBuku[0].judul)
	/*
		2. Tambahkan 4 buku seperti contoh gambar, data tahun dan penulis bebas
			Buku = A C ZZ K
	*/
	tambahBuku(&TabBuku, &Kardus, &Outermost)
	//ambilBuku(&TabBuku, &Kardus, &Outermost)
	/*
		3. Cari buku dengan judul “C”, harusnya yang tampil adalah K dan ZZ, KETEMU
	*/
	cariBuku("C", &TabBuku, &Kardus, &Outermost)
	//fmt.Println(Kardus, Outermost)
	/*
		4. Tambahkan buku sampai kardus penuh
	*/
	tambahBuku(&TabBuku, &Kardus, &Outermost)
	/*
		5. Cari buku dengan judul yang tidak terdapat pada kardus tersebut.
	*/
	cariBuku("ABC", &TabBuku, &Kardus, &Outermost)
}

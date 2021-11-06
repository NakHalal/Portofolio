package main

import "fmt"

/*
procedure isiArray(in/out t:tabel, n:integer)
{IS. Data tersedia dalam piranti masukan
FS. Array t berisi sejumlah n karakter yang dimasukkan user,
Proses input selama karakter bukanlah TITIK dan n <= NMAX}
procedure cetakArray(in t:tabel, n:integer)
{IS. Terdefinisi array t yang berisi sejumlah n karakter
FS. n karakter dalam array muncul di layar}
procedure balikanArray(in/out t:tabel, in n:integer)
{IS. Terdefinisi array t yang berisi sejumlah n karakter
FS. Urutan isi array t terbalik }
function palindrom(t:tabel, n:integer) -> Boolean
{Mengembalikan true apabila susunan karakter didalam t membentuk
palindrom, dan false apabila sebaliknya. Petunjuk: Manfaatkan prosedur
balikanArray}
*/

func isiArray(NMAX *int, tabel *[127]string, n *int) {
	var X string
	var i int
	fmt.Print("Teks: ")
	for X != "." && i < (*NMAX-1) {
		fmt.Scan(&X)
		if X != "." && i < (*NMAX-1) {
			tabel[i] = X
			i += 1
		}
	}
	*n = i
}

func cetakArray(tabel *[127]string, n *int) {
	for i := 0; i < (*n); i++ {
		fmt.Print(tabel[i])
	}
	fmt.Println()
}

func balikanArray(tabel *[127]string, n *int, tabelori *[127]string) {
	*tabelori = *tabel
	for i, j := 0, (*n - 1); i < j; i, j = i+1, j-1 {
		tabel[i], tabel[j] = tabel[j], tabel[i]
	}
}

func palindrom(tabel [127]string, n int, tabelori [127]string) bool {
	if tabel == tabelori {
		return true
	} else {
		return false
	}
}

func main() {
	var NMAX int = 127
	var tabel [127]string
	var tabelori [127]string
	var n int
	isiArray(&NMAX, &tabel, &n)
	//cetakArray(&tabel, &n)
	balikanArray(&tabel, &n, &tabelori)
	//cetakArray(&tabel, &n)
	fmt.Println("Palindrom ? ", palindrom(tabel, n, tabelori))
	//fmt.Println(tabel, tabelori)
}

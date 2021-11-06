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

const NMAX int = 127

type tabel [NMAX]string

func isiArray(A *tabel, n *int) {
	var X string
	var i int
	fmt.Print("Inputkan Teks dengan Spasi Setiap Huruf: ")
	for X != "." && i < (NMAX-1) {
		fmt.Scan(&X)
		if X != "." && i < (NMAX-1) {
			A[i] = X
			i += 1
		}
	}
	*n = i
}

func cetakArray(A *tabel, n *int) {
	for i := 0; i < (*n); i++ {
		fmt.Print(A[i])
	}
	fmt.Println()
}

func balikanArray(A *tabel, n *int, B *tabel) {
	*B = *A
	for i, j := 0, (*n - 1); i < j; i, j = i+1, j-1 {
		A[i], A[j] = A[j], A[i]
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
	var A, B tabel
	var n int
	isiArray(&A, &n)
	//ori = cetakArray(&B, &n)
	//balik = cetakArray(&A, &n)
	balikanArray(&A, &n, &B)
	fmt.Println("Palindrom ? ", palindrom(A, n, B))
	fmt.Print("Teks Original: ")
	cetakArray(&B, &n)
	fmt.Print("Teks Dibalilk: ")
	cetakArray(&A, &n)
}

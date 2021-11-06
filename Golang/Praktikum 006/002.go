package main

import (
	"fmt"
)

//deklarasi variable
var d2, d3, d4 int

//fungsi pangkat
func pangkat(n int) int {
	//deklarasi variable
	var hasil int

	//set variable ke angka yang sesuai
	hasil = 1

	//perulangan untuk memangkatkan 2 dengan n
	for i := 1; i < n; {
		hasil = 2 * hasil
		i++
	}

	//keluaran dari fungsi pangkat
	return hasil
}

//procedure cariDigit
func cariDigit(n int) {
	//deklarasi variable
	var now int

	//langkah menentukan digit 2, 3, dan 4
	now = n
	d4 = now % 10
	now = now / 10
	d3 = now % 10
	now = now / 10
	d2 = now % 10
}

//main program
func main() {
	//deklarasi variable
	var x int
	var d1 int = 1

	//input angka biner yang akan dikonversi
	fmt.Scan(&x)

	//jalankan procedure cariDigit()
	cariDigit(x)

	//output hasil konversi biner ke desimal
	fmt.Print(d1*pangkat(4) + d2*pangkat(3) + d3*pangkat(2) + d4*pangkat(1))
}

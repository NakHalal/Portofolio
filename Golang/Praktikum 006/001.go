package main

import "fmt"

//deklarasi variable
var mi, ma, f1, f2 int

//procedure min
func min(f1 int) {
	//percabangan untuk menentukan keluaran f2
	if f1 <= mi {
		f2 = f1
	} else {
		f2 = mi
	}
}

//procedure max
func max(f1 int) {
	//percabangan untuk menentukan keluaran f2
	if f1 >= ma {
		f2 = f1
	} else {
		f2 = ma
	}
}

//main program
func main() {
	//deklarasi variable
	var jml, x int

	//set variable ke angka yang sesuai
	ma = 0
	mi = 0

	//input jumlah bilangan yang akan dicek
	fmt.Scan(&jml)

	//perulangan
	for i := 1; i <= jml; {
		fmt.Scan(&x)
		//panggil procedure min()
		min(x)
		//masukkan f2 ke mi
		mi = f2
		//panggil procedure max()
		max(x)
		//masukkan f2 ke ma
		ma = f2
		i++
	}

	//output bilangan terbesar dan bilangan terkecil
	fmt.Print(ma, mi)
}

package main

import "fmt"

const NMAX = 100

type mahasiswa struct {
	nama   string
	tinggi int
}

type dataMhs [NMAX]mahasiswa

func main() {
	var XYZ dataMhs
	var n int

	fmt.Scan(&n)
	bacaData(&XYZ, &n)
	urutData(&XYZ, n)
	cetakData(XYZ, n)
}

func bacaData(XYZ *dataMhs, n *int) {
	/* IS. n data mahasiswa telah siap pada piranti masukan
	FS. menerima input n dan array t berisi n data tinggi mahasiswa */
	var Y int
	var X string

	for i := 0; i < *n; i++ {
		fmt.Scan(&X, &Y)
		XYZ[i].nama = X
		XYZ[i].tinggi = Y
	}
}

func cetakData(XYZ dataMhs, n int) {
	/* IS. terdefinisi sebuah array t yang berisi n data tinggi mahasiswa
	   FS. menampilkan array t ke layar monitor */
	fmt.Println("——————————")
	for i := 0; i < n; i++ {
		fmt.Println(XYZ[i].nama, XYZ[i].tinggi)
	}
}

func urutData(XYZ *dataMhs, n int) {
	/* IS. terdefinisi sebuah array t yang berisi n data tinggi mahasiswa
	FS. array t terurut ascending berdasarkan tinggi dengan algoritma selection sort
	*/
	for i := 0; i < n-1; i++ {
		minIndex := i
		for j := i + 1; j < n; j++ {
			if XYZ[j].tinggi < XYZ[minIndex].tinggi {
				XYZ[j], XYZ[minIndex] = XYZ[minIndex], XYZ[j]
			}
		}
	}
}

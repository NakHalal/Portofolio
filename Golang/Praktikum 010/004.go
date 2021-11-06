package main

import "fmt"

const NMAX = 1000000

var data [NMAX]int

func isiArray(n *int) {
	/* IS. Data n sudah siap pada piranti masukan.
	   FS. Array data berisi n (<=NMAX) bilangan */
	var jk int
	for i := 0; i < *n; i++ {
		fmt.Scan(&jk)
		data[i] = jk
	}
}

func posisi(n, k int) int {
	/* mengembalikan posisi k dalam array data dengan n elemen.
	Posisi dimulai dari posisi 0. Jika tidak ada kembalikan -1 */
	var fy int = -1
	for i := 0; i < n; i++ {
		if data[i] == k {
			fy = i
		}
	}
	return fy
}

func main() {
	/* buatlah kode utama yang membaca baris pertama (n dan k). kemudian data diisi
	oleh prosedur isiArray(n), dan pencarian oleh fungsi posisi(n,k),
	dan setelah itu output dicetak.*/
	var n, k int
	fmt.Scan(&n, &k)
	isiArray(&n)

	if posisi(n, k) != -1 {
		fmt.Println(posisi(n, k))
	} else {
		fmt.Println("Not Found")
	}
}

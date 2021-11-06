package main

import "fmt"

func main() {
	var TAB [100]int
	var n, u, d int

	fmt.Scan(&n, &d, &u)
	isiArray(&TAB, &n)
	sorting(&TAB, u, d, n)
	tampilArray(TAB, n)
}

func isiArray(TAB *[100]int, n *int) {
	/* IS. terdefinisi bilangan bulat n, dan n buah bilangan bulat telah siap pada piranti masukan
	FS. array t berisi n buah bilangan bulat yang berasal dari user */
	var X int

	for i := 0; i < *n; i++ {
		fmt.Scan(&X)
		TAB[i] = X
	}
}

func tampilArray(TAB [100]int, n int) {
	/* IS. terdefinisi sebuah array t yang berisi n buah bilang bulat
	FS. menampilkan array t ke layar secara horizontal */
	for i := 0; i < n; i++ {
		fmt.Print(TAB[i], " ")
	}
}

func sorting(TAB *[100]int, u, d, n int) {
	/* IS. terdefinisi sebuah array t yang berisi n bilangan bulat, dan indeks bilangan bulat u dan d
	FS. array t terurut descending dari indeks ke-d hingga ke-u dengan menggunakan algoritma insertion sort */
	for i := d + 1; i < u; i++ {
		var j int = i
		for j > d {
			if TAB[j-1] < TAB[j] {
				TAB[j-1], TAB[j] = TAB[j], TAB[j-1]
			}
			j--
		}
	}
}

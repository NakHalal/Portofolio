package main

import "fmt"

func main() {
	//deklarasi
	var A, AGK1, AGK2 int

	//input jumlah pasangan data
	fmt.Scanln(&A)

	//cek ganjil genap nentukan dan outputkan rahasia
	for i := 1; i <= A; i = i + 1 {
		fmt.Scanln(&AGK1, &AGK2)
		if (AGK1+AGK2)%2 == 0 {
			fmt.Println(AGK1)
		} else if (AGK1+AGK2)%2 != 0 {
			fmt.Println(AGK2)
		}
	}
}

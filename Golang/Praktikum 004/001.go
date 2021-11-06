package main

import (
	"fmt"
)

func main() {
	//deklarasi
	var A int
	var FKTR []int

	//input angka yg dicek
	fmt.Scanln(&A)

	//output faktor
	for i := 1; i <= A; i++ {
		if A%i == 0 {
			fmt.Print(i, " ")
			FKTR = append(FKTR, i)
		}
	}

	//cek apakah oleole
	if len(FKTR) > 2 {
		fmt.Println("\nBukan Oleole")
	} else {
		fmt.Println("\nOleole")
	}
}

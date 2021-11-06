package main

import "fmt"

func main() {
	var A, hasil float64

	fmt.Scanln(&A)
	hasil = float64(22) / float64(7) * float64(A)
	fmt.Println("Luas lingkaran dengan jari-jari =", A, "adalah", hasil)
}

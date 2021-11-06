package main

import "fmt"

func main() {
	var A string
	var B, C, hasil int

	fmt.Scanln(&A, &B, &C)
	hasil = B + C
	fmt.Println("Kata =", A)
	fmt.Println("Jumlah =", hasil)
}

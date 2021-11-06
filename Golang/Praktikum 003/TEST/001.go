package main

import "fmt"

func main() {
	var A, B, C, D, E int
	var F int

	fmt.Scanf("%c", &A)
	fmt.Scanf("%c", &B)
	fmt.Scanf("%c", &C)
	fmt.Scanf("%c", &D)
	fmt.Scanf("%c\n", &E)

	fmt.Scanln(&F)

	fmt.Printf("%c", A+F)
	fmt.Printf("%c", B+F)
	fmt.Printf("%c", C+F)
	fmt.Printf("%c", D+F)
	fmt.Printf("%c", E+F)
}

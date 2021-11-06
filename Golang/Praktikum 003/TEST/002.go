package main

import "fmt"

func main() {
	var A, B, C, D int

	fmt.Scanf("%c", &A)
	fmt.Scanf("%c", &B)
	fmt.Scanf("%c", &C)
	fmt.Scanf("%c\n", &D)

	fmt.Printf("%c\n", A)
	fmt.Printf("%c\n", B)
	fmt.Printf("%c\n", C)
	fmt.Printf("%c\n", D)

	fmt.Printf("%c%c\n", A, B)
	fmt.Printf("%c%c\n", B, C)
	fmt.Printf("%c%c\n", C, D)

	fmt.Printf("%c%c%c\n", A, B, C)
	fmt.Printf("%c%c%c\n", B, C, D)

	fmt.Printf("%c%c%c%c\n", A, B, C, D)
}

package main

import "fmt"

func main() {
	var A, B, C, D, E int
	var F, G, H int

	fmt.Scanln(&A, &B, &C, &D, &E)
	fmt.Scanf("%c", &F)
	fmt.Scanf("%c", &G)
	fmt.Scanf("%c", &H)
	fmt.Printf("%c", A)
	fmt.Printf("%c", B)
	fmt.Printf("%c", C)
	fmt.Printf("%c", D)
	fmt.Printf("%c\n", E)
	fmt.Printf("%c", F+1)
	fmt.Printf("%c", G+1)
	fmt.Printf("%c", H+1)
}

package main

import "fmt"

func main() {
	var A, B, C, D, E int
	var F, G, H, I, J string

	fmt.Scanf("%2v%1s", &A, &F)
	fmt.Scanf("%2v%1s", &B, &G)
	fmt.Scanf("%2v%1s", &C, &H)
	fmt.Scanf("%2v%1s", &D, &I)
	fmt.Scanf("%2v%1s", &E, &J)

	fmt.Printf("%v %s\n", A, F)
	fmt.Printf("%v %s\n", B, G)
	fmt.Printf("%v %s\n", C, H)
	fmt.Printf("%v %s\n", D, I)
	fmt.Printf("%v %s\n", E, J)

	fmt.Println()
}

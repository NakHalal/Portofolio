package main

import "fmt"

func main() {
	var A, B, C, D, E int
	var F, G, H, I, J string

	fmt.Scanf("%2d%1s", &A, &F)
	fmt.Scanf("%2d%1s", &B, &G)
	fmt.Scanf("%2d%1s", &C, &H)
	fmt.Scanf("%2d%1s", &D, &I)
	fmt.Scanf("%2d%1s", &E, &J)

	fmt.Println((A == B && B == C && C == D) || (B == C && C == D && D == E) || (C == D && D == E && E == A) || (D == E && E == A && A == B) || (E == A && A == B && B == C))
}

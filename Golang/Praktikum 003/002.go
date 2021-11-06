package main

import "fmt"

func main() {
	var A, B, C, D int
	var E, F, G int
	var H, I, J, K int

	fmt.Scanf("%c", &A)
	fmt.Scanf("%c", &B)
	fmt.Scanf("%c", &C)
	fmt.Scanf("%c\n", &D)

	fmt.Scanf("%c\n", &E)
	fmt.Scanf("%c%c\n", &F, &G)
	fmt.Scanf("%c%c%c%c\n", &H, &I, &J, &K)

	fmt.Println(H == A && I == B && J == C && K == D)
	fmt.Println(E == A || E == B || E == C || E == D)
	fmt.Println((F == A && G == B) || (F == B && G == C) || (F == C && G == D))
}

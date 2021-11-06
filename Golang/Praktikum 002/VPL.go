package main

import "fmt"

func main() {
	var A, B int

	fmt.Scanln(&A, &B)
	for i := A; i < B+1; i++ {
		fmt.Printf("Simbol ASCII dari %d adalah %c\n", i, i)
	}
}

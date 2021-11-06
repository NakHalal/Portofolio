package main

import (
	"fmt"
	"strconv"
)

func main() {
	var A, B int
	var Total string
	B = 0
	Total = ""

	fmt.Scanln(&A)
	for i := 0; i < A; {
		fmt.Scanln(&B)
		if B >= 0 && B < 10 {
			B := strconv.Itoa(B)
			Total = B + Total
			i++
		}
	}
	fmt.Print(Total)
}

package main

import "fmt"

func main() {
	var A int

	fmt.Scanln(&A)
	if A%3 == 0 {
		fmt.Println("Fizz")
	}
	if A%5 == 0 {
		fmt.Println("Bazz")
	}
}

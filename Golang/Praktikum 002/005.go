package main

import "fmt"

func main() {
	var A string

	fmt.Scanln(&A)
	for A != "selesai" {
		fmt.Println(A)
		fmt.Scanln(&A)
	}
}

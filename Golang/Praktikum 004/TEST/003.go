package main

import "fmt"

func main() {
	var n, angka1, angka2 int
	fmt.Scanln(&n)
	for angka1 != -1 && angka2 != -1 {
		fmt.Scanln(&angka1, &angka2)
		if angka1%n == 0 {
			fmt.Println(angka2)
		}
		if angka2%n == 0 {
			fmt.Println(angka1)
		}
	}
}

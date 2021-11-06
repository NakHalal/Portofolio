package main

import (
	"fmt"
)

var n, i, k, toti, totk int

func main() {
	i := 1
	for k < 5 {
		fmt.Scan(&n)
		if n%i == 0 {
			k += 1
			toti += i
			totk += n
		}
		i += 1
	}
	fmt.Println("Jumlah Bilangan Adalah", totk)
	fmt.Println("Jumlah Posisi Adalah", toti)
}

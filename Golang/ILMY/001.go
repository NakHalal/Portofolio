package main

import (
	"fmt"
	"strings"
)

var lapar, jatcin bool
var warna string

func main() {
	fmt.Print("Warna Kucing: ")
	fmt.Scan(&warna)
	warna = strings.ToLower(warna)
	if warna != "hitam" {
		fmt.Print("Kucing Lapar? (True/False) ")
		fmt.Scan(&lapar)
		fmt.Print("Kucing Jatuh Cinta? (True/False) ")
		fmt.Scan(&jatcin)
		if lapar || jatcin {
			fmt.Print("Kucing Mengeong")
		} else {
			fmt.Print("Kucing Membisu")
		}
	} else {
		fmt.Print("Kucing Membisu")
	}
}

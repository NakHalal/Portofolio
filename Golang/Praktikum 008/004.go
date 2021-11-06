package main

import "fmt"

func hitungNopol(noPol string, kodeJKT, kodeBDG, kodeLUAR *int) {
	if noPol == "B" || noPol == "F" {
		*kodeJKT += 1
	} else if noPol == "D" || noPol == "Z" {
		*kodeBDG += 1
	} else if noPol == "." {
		// do Nothing
	} else {
		*kodeLUAR += 1
	}
}

func main() {
	var noPol string
	var BDG, JKT, LUAR int
	for noPol != "." {
		fmt.Scan(&noPol)
		hitungNopol(noPol, &JKT, &BDG, &LUAR)
	}
	fmt.Print(BDG, " ", JKT, " ", LUAR)
}

package main

import (
	"fmt"
)

//deklarasi variable
var biner, hasil string
var desimal, result, remainder int

//procedure Division untuk menentukan result dan remainder
func Division(a int, b int) {
	result = a / b
	remainder = a % b
}

//fungsi ubah angka ke string
func Num2Str(x int) string {
	if x == 0 {
		return "0"
	} else if x == 1 {
		return "1"
	} else {
		return ""
	}
}

//function ubah desimal ke binary
func Des2Bin(desimal int) string {
	hasil = ""
	for desimal > 0 {
		Division(desimal, 2)
		desimal = result
		hasil = Num2Str(remainder) + hasil
	}
	return hasil
}

//program utama
func main() {
	fmt.Scan(&desimal)
	biner = Des2Bin(desimal)
	print(biner)
}

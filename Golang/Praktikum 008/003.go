package main

import "fmt"

var R int
var S int

func kpk(y int, z int) int {
	return ((y * z) / ppb(y, z))
}

func ppb(y int, z int) int {
	for z != 0 {
		temp := z
		z = y % z
		y = temp
	}
	return y
}

func main() {
	fmt.Scan(&R, &S)
	fmt.Print(kpk(R, S))
}

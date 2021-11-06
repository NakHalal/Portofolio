package main

import "fmt"

func hitungSuara(suara int, iniA, iniB, iniC *int) {
	if suara == 1 {
		*iniA += 1
	} else if suara == 2 {
		*iniB += 1
	} else if suara == 3 {
		*iniC += 1
	}
}

func main() {
	var n int
	var a, b, c int
	for n != -1 {
		fmt.Scan(&n)
		hitungSuara(n, &a, &b, &c)
	}
	fmt.Print(a, " ", b, " ", c)
}

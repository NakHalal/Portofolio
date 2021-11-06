package main

import (
	"fmt"
)

var kktn, i int

func main() {
	i := 1
	fmt.Print("Berapa Kekuatan Awal Gerbang? ")
	fmt.Scan(&kktn)
	fmt.Println("Berapa Kekuatan Awal Gerbang: ", kktn)
	for kktn-3 > 0 {
		kktn -= 3
		i += 1
		fmt.Println("dobrak, sisa kekuatan ", kktn)
	}
	fmt.Println("dobrak, gerbang jebol")
	fmt.Println("Pasukan berusaha sebanyak", i, "kali")
}

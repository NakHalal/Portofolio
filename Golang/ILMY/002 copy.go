package main

import (
	"fmt"
)

var kktn int

func main() {
	fmt.Print("Berapa Kekuatan Awal Gerbang? ")
	fmt.Scan(&kktn)
	fmt.Println("Berapa Kekuatan Awal Gerbang: ", kktn)
	if kktn-3 > 0 {
		kktn -= 3
		fmt.Println("dobrak, sisa kekuatan ", kktn)
		if kktn-3 > 0 {
			kktn -= 3
			fmt.Println("dobrak, sisa kekuatan ", kktn)
			if kktn-3 > 0 {
				kktn -= 3
				fmt.Println("dobrak, sisa kekuatan ", kktn)
				if kktn-3 > 0 {
					kktn -= 3
					fmt.Println("dobrak, sisa kekuatan ", kktn)
				} else {
					fmt.Println("dobrak, gerbang jebol")
				}
			} else {
				fmt.Println("dobrak, gerbang jebol")
			}
		} else {
			fmt.Println("dobrak, gerbang jebol")
		}
	} else {
		fmt.Println("dobrak, gerbang jebol")
	}
}

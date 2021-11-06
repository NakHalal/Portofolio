package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var seed int64
	var tebak1, tebak2 string
	var rahasia int

	fmt.Print("Angka Rahasia: ")
	fmt.Scanln(&seed)
	rand.Seed(seed)

	rahasia = rand.Intn(6) + 1

	fmt.Print("Anda: ")
	fmt.Scanln(&tebak1, &tebak2)

	rahasia = 1
	if tebak1 == "genap" {
		if tebak2 == "kecil" {
			if rahasia == 2 {
				fmt.Print("Nilai dadu ", rahasia, ", Anda benar")
			} else {
				fmt.Print("Nilai dadu ", rahasia, ", Anda kalah")
			}
		}
		if tebak2 == "besar" {
			if rahasia == 4 || rahasia == 6 {
				fmt.Print("Nilai dadu ", rahasia, ", Anda benar")
			} else {
				fmt.Print("Nilai dadu ", rahasia, ", Anda kalah")
			}
		}
	} else if tebak1 == "ganjil" {
		if tebak2 == "kecil" {
			if rahasia == 1 || rahasia == 3 {
				fmt.Print("Nilai dadu ", rahasia, ", Anda benar")
			} else {
				fmt.Print("Nilai dadu ", rahasia, ", Anda kalah")
			}
		}
		if tebak2 == "besar" {
			if rahasia == 5 {
				fmt.Print("Nilai dadu ", rahasia, ", Anda benar")
			} else {
				fmt.Print("Nilai dadu ", rahasia, ", Anda kalah")
			}
		}
	} else {
		fmt.Print("Nilai dadu ", rahasia, ", Anda kalah")
	}
}

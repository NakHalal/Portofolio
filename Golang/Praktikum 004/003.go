package main

import (
	"fmt"
	"math/rand"
)

func main() {
	//deklarasi
	var seed, sx int64
	var tebak int
	var rahasia int
	var Dadang int

	//input angka rahasia untuk dijadikan seed random
	fmt.Print("Angka Rahasia: ")
	fmt.Scanln(&seed)
	rand.Seed(seed)

	//generate dadu rahasia
	rahasia = rand.Intn(6) + 1

	//ubah rahasia dari int ke int64
	sx = int64(rahasia)

	//ubah seed agar dadu rahasia dengan dadu Dadang tidak selalu sama
	seed = seed - sx
	rand.Seed(seed)

	//generate dadu Dadang
	Dadang = rand.Intn(6) + 1

	//input tebakan player
	fmt.Print("Anda: ")
	fmt.Scanln(&tebak)

	//output tebakan Dadang
	fmt.Print("Dadang: ", Dadang, "\n")

	//cek kebenaran dadu Player, Dadang, dan Rahasia + Output hasil
	if tebak == rahasia && Dadang != rahasia {
		fmt.Print("Nilai dadu ", rahasia, ", Pemenang adalah anda")
	} else if tebak != rahasia && Dadang == rahasia {
		fmt.Print("Nilai dadu ", rahasia, ", Pemenang adalah Dadang")
	} else if tebak == rahasia && Dadang == rahasia {
		fmt.Print("Nilai dadu ", rahasia, ", Seri")
	} else {
		fmt.Print("Nilai dadu ", rahasia, ", Tidak ada pemenang")
	}
}

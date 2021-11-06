package main

import (
	"fmt"
)

func main() {
	//deklarasi variable
	var angka, i, bil, total int

	//set variable ke angka yang sesuai untuk digunakan didalam perulangan
	i = 1
	bil = 0
	angka = 1

	//perulangan
	for angka > 0 {
		//output
		fmt.Print("Bilangan ke-", i, ": ")

		//input angka
		fmt.Scan(&angka)

		//cek apakah angka bukan 0, jika 0 maka hentikan perulangan
		if angka == 0 {
			break
		}

		//jika angka yang dimasukkan negatif maka akan diminta input lagi sampai positif
		for !(angka > 0) {
			//output
			fmt.Print("Bilangan ke-", i, ": ")

			//input angka
			fmt.Scan(&angka)

			//cek apakah angka bukan 0, jika 0 maka hentikan perulangan
			if angka == 0 {
				break
			}
		}
		//cek apakah angka bukan 0, jika 0 maka hentikan perulangan
		if angka == 0 {
			break
		}
		//cek apakah hasil bagi antara angka dengan baris adalah 0 (cek kelipatan)
		//jika ternyata benar kelipatannya maka jumlahkan kedalam variable total
		if angka%i == 0 {
			bil = bil + 1
			total = total + angka
		}
		i++
	}
	//outputkan banyak bilangan yang pengecekan kelipatannya benar
	//outputlam total penjumlahan bilangan yang pengecekan kelipatannya benar
	fmt.Print("Banyaknya bilangan ", bil, "\n")
	fmt.Print("Total penjumlahan ", total, "\n")
}

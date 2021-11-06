package main

import (
	"fmt"
)

func main() {
	//deklarasi
	var dominasi, netral, positif, A, B int

	//set variable ke angka yang sesuai untuk digunakan didalam perulangan
	dominasi = 0
	netral = 0
	positif = 0

	//perulangan
	for dominasi == 0 {
		//input angka positif dan negatif
		fmt.Scan(&A, &B)

		//pengecekan apakah energi negatif lebih besar daripada energi positif atau netral
		if A+B == 0 {
			netral = netral + 1
		} else if A+B > 0 {
			positif = positif + 1
		} else if A+B < 0 {
			dominasi = 1
		}
	}

	//output hasil netral dan positif
	fmt.Print("Netral : ", netral, "\n")
	fmt.Print("Positif : ", positif, "\n")
}

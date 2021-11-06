package main

import "fmt"

func main() {
	var nilai, n, jumlah, rata2 float64

	n = 0
	fmt.Scanln(&nilai)
	for nilai != -1 {
		n = n + 1
		jumlah = jumlah + nilai
		fmt.Scanln(&nilai)
	}
	if n == 0 {
		rata2 = 0.0
	} else {
		rata2 = jumlah / n
	}
	fmt.Println(rata2)

}

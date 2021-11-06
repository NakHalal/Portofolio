package main

import "fmt"

func main() {
	var A, B, C, D int

	fmt.Scanln(&A, &B, &C, &D)
	if int(D) > int(A) && int(D) > int(B) && int(D) > int(C) {
		fmt.Println("Ada rekor baru")
	} else {
		fmt.Println("Tidak ada rekor baru")
	}
}

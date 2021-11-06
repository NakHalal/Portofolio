package main

import (
	"fmt"
)

func main() {
	var A, B, C, Total int
	Total = 0
	C = 0
	fmt.Scanln(&A)
	for i := 0; i < A; {
		fmt.Scanf("%d", &B)
		if B >= 0 && B <= 100 {
			if B >= C && B != 0 {
				if B != C {
					Total = 0
				}
				C = B
				Total = Total + 1
				//fmt.Print(C)
			}
			i++
		}
	}
	fmt.Print("Nilai terbesar adalah ", B, " yang diperoleh ", Total, " orang mahasiswa")
}

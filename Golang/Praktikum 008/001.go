package main

import "fmt"

var codeA, codeB, n, brbA, brbB int
var key bool

func main() {
	fmt.Scan(&n, &codeA, &codeB)
	brbA = (n % codeA)
	brbB = (n % codeB)
	key = (brbA == brbB)
	if codeA == codeB {
		fmt.Print("Kita tidak pernah bertemu")
	} else if (n%codeB == 0 || n%codeA == 0) && !key {
		fmt.Print("Kita bertemu hari ini")
	} else if (n%codeB == 0 || n%codeA == 0) && key {
		fmt.Print("Kita bertemu 7 hari lagi")
	} else {
		if (codeA - brbA) < (codeB - brbB) {
			fmt.Print("Kita bertemu ", (codeA - brbA), " hari lagi")
		} else if (codeA - brbB) < (codeB - brbA) {
			fmt.Print("Kita bertemu ", (codeA - brbB), " hari lagi")
		}
	}
}

package main

import "fmt"

/*
func scanthis(A *[123]int, B *[123]int, C *[123]int, timke *int) {
	var hehe, i int
	i = 0
	fmt.Scan(&hehe)
	for hehe > 0 {
		fmt.Scan(&hehe)
		if hehe > 0 {
			if *timke == 1 {
				//A = append(hehe, i)
				A[i] = hehe
			} else if *timke == 2 {
				B[i] = hehe
			} else if *timke == 3 {
				C[i] = hehe
			}
		}
		i += 1
	}
	*timke += 1
}
*/

type menang struct {
	A int
}

func main() {
	A := []menang{}
	A = append(A, menang{3})
	fmt.Print(A[0])
	var B int
	B += menang{A}
	fmt.Print(B)
	//var A, B, C [123]int
	/*
		var timke int
		timke = 1
		scanthis(&A, &B, &C, &timke)
		fmt.Print(len(A))
	*/
}

package main

import "fmt"

func inputData(A *[]int, B *[]int, C *[]int, timke *int, n *int, rataA *float64, rataB *float64, rataC *float64) {
	var hehe, i int
	i = 0
	*n = 0
	hehe = 1
	for hehe > 0 {
		fmt.Scan(&hehe)
		if hehe > 0 {
			if *timke == 1 {
				*A = append(*A, hehe)
				*n = len(*A)
				*rataA = rataan(A, n)
			} else if *timke == 2 {
				*B = append(*B, hehe)
				*n = len(*B)
				*rataB = rataan(A, n)
			} else if *timke == 3 {
				*C = append(*C, hehe)
				*n = len(*C)
				*rataC = rataan(A, n)
			}
		}
		i += 1
	}
	*timke += 1
}

func rataan(X *[]int, n *int) float64 {
	var totalX int
	var totalY, length float64
	for a1 := 0; a1 < (len(*X) - 1); a1++ {
		totalX += (*X)[a1]
	}
	totalY = float64(totalX)
	length = float64(*n)
	return (totalY / length)
}

func main() {
	var A, B, C []int
	var rataA, rataB, rataC float64
	var timke, n int
	timke = 1
	for i := 0; i < 3; i++ {
		inputData(&A, &B, &C, &timke, &n, &rataA, &rataB, &rataC)
	}

	fmt.Println(rataA, rataB, rataC)
}

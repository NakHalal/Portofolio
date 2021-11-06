package main

import "fmt"

type tabgol = [100]int

func inputData(A *tabgol, B *tabgol, C *tabgol, timke *int, n *int, rataA *float64, rataB *float64, rataC *float64) {
	var hehe int
	//i = 0
	*n = 0
	hehe = 1
	if *timke == 1 {
		k := 0
		for hehe > 0 {
			fmt.Scan(&hehe)
			if hehe > 0 {
				A[k] = hehe
				k++
			}
		}
		*rataA = rataan(A, &k)
	} else if *timke == 2 {
		k := 0
		for hehe > 0 {
			fmt.Scan(&hehe)
			if hehe > 0 {
				B[k] = hehe
				k++
			}
		}
		*rataB = rataan(B, &k)
	} else if *timke == 3 {
		k := 0
		for hehe > 0 {
			fmt.Scan(&hehe)
			if hehe > 0 {
				C[k] = hehe
				k++
			}
		}
		*rataC = rataan(C, &k)
	}
	*timke++
}

func rataan(X *tabgol, n *int) float64 {
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
	var A, B, C tabgol
	var rataA, rataB, rataC float64
	var timke, n int
	timke = 1
	for i := 0; i < 3; i++ {
		inputData(&A, &B, &C, &timke, &n, &rataA, &rataB, &rataC)
	}

	fmt.Println(rataA, rataB, rataC)
}

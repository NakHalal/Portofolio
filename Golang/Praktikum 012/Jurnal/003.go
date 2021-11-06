package main

import (
	"fmt"
)

const NMAX = 1000000

var tabDate [NMAX]string

var n int

func main() {
	//{panggil procedure addData di sini}
	addData(&tabDate, &n)
	//{panggil procedure urut di sini}
	urut(&tabDate, n)
	//{panggil procedure printData di sini}
	PrintData(tabDate, n)

}

func addData(list *[NMAX]string, n *int) {
	var X string
	fmt.Scan(&X)
	for i := 0; X != "####.##.##"; i++ {
		list[i] = X
		fmt.Scan(&X)
		*n = i
	}
}

func urut(list *[NMAX]string, n int) {
	var i int = 0
	var IDX int = maxPos(tabDate, i, n)
	for i < n {
		swap(&list[i], &list[IDX])
		i += 1
		IDX = maxPos(tabDate, i, n)
		//fmt.Println(tabDate)
	}
}

func maxPos(list [NMAX]string, start int, n int) int {
	var result int
	var max string
	max = list[start]
	result = start
	start++
	for start <= n {
		if list[start] > max {
			max = list[start]
			result = start
		}
		start++
	}
	return result
}

func swap(x *string, y *string) {
	*x, *y = *y, *x
}

func PrintData(list [NMAX]string, n int) {
	for i := 0; i <= n; i++ {
		fmt.Print(list[i], "\n")
	}
}

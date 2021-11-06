package main

import "fmt"

const NMAX = 1000000
type tabDate [NMAX] string

func addData( list *tabDate, n *int) {
	var input string
	
	fmt.Scanln(&input)
	for input != "####.##.##" {
		list[*n] = input
		*n++
		ftm.Scanln(&input)
	}
}

func urut(list *tabDate, n int) {
	var i, idx, int
	i = 0
	for i < n-1 {
		idx = maxPos(list, i, n)
		swap(list[])
	}
}

func maxPos( list *tabDate, start, n int)int {
	var result int
	var max string
	max = list[start]
	result = start
	start++
	for start < n {
		if list[start] > max {
			max = list[start]
			result = start

		}
		start++
	}
	return result
}

func swap(x,y *string){
	var temp string
	temp = *x
	*x = *y
	*y = temp
}

func printData(list tabDate, n int){
	for i:=0;i<n;i++{
		fmt.Println(list[i])
	}
}

func main(){
	var t tabDate
	var n int
	addData(&t,&n)
	urut(&t, n)
	printData(t,n)
}
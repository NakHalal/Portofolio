package main

import "fmt"

var C string = "2021.23.12"
var D string = "2022"

func main() {
	fmt.Println(C[0], C[1], C[2], C[3])
	fmt.Println(D[0], D[1], D[2], D[3])
	fmt.Println(string(C[0:4] + C[5:7] + C[8:10]))
	fmt.Println("2015.03.02" > "2008.01.14")
}

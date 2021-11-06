package main

import (
	"fmt"
	"math"
)

//function jarak(a,b,c,d : real) -> real
//{Mengembalikan jarak antara titik (a,b) dan titik (c,d)}
func jarak(a, b, c, d float64) float64 {
	//keluaran dari fungsi jarak
	return math.Sqrt((math.Pow((a - c), 2)) + (math.Pow((b - d), 2)))
}

//function posisi(cx,cy,r,x,y : real) -> boolean
//{Mengembalikan true apabila titik (x,y) berada di dalam lingkaran yang memiliki titik pusat (cx,cy) dan radius r}
func posisi(cx, cy, r, x, y float64) bool {
	//deklarasi variable
	var A float64

	//memasukkan hasil dari jarak(x, y, cx, cy) ke variable A
	A = jarak(x, y, cx, cy)

	//percabangan
	if A < r {
		//keluaran dari fungsi posisi jika A < r
		return true
	} else {
		//keluaran dari fungsi posisi jika !(A < r)
		return false
	}
}

//main program
func main() {
	//deklarasi variable
	var x, y, r, cx, cy float64

	//inputan baris pertama
	fmt.Scanln(&x, &y, &r)

	//inputan baris kedua
	fmt.Scanln(&cx, &cy)

	//percabangan
	if posisi(x, y, r, cx, cy) {
		//output jika posisi == true
		fmt.Print("Anda berada di dalam taman")
	} else {
		//output jika posisi != true
		fmt.Print("Anda berada di luar taman")
	}
}

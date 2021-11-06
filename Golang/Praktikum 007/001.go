package main

import (
	"fmt"
	"math"
)

var ax, ay, ar, bx, by, br float64
var t1, t2 float64
var jarak float64

func Jarak(ax float64, ay float64, bx float64, by float64) float64 {
	return (math.Sqrt((math.Pow((ax - bx), 2)) + (math.Pow((ay - by), 2))))
}

func Lingkaran(t1 float64, t2 float64, x1 float64, y1 float64, r1 float64) bool {
	var tes float64
	tes = Jarak(t1, t2, x1, y1)
	if tes < r1 {
		return true
	} else {
		return false
	}
}

func cariTeks() {
	if Lingkaran(t1, t2, ax, ay, ar) && Lingkaran(t1, t2, bx, by, br) {
		fmt.Print("di dalam lingkaran 1 dan 2")
	} else if Lingkaran(t1, t2, ax, ay, ar) {
		fmt.Print("di dalam lingkaran 1")
	} else if Lingkaran(t1, t2, bx, by, br) {
		fmt.Print("di dalam lingkaran 2")
	} else {
		fmt.Print("di luar lingkaran 1 dan 2")
	}
}

func main() {
	//fmt.Print(math.Pow(5, 2))
	fmt.Scan(&ax, &ay, &ar)
	fmt.Scan(&bx, &by, &br)
	fmt.Scan(&t1, &t2)
	cariTeks()
}

package main

import (
	"fmt"
)

func f(x float64) float64 {
	//keluaran dari fungsi f
	return x * x
}

func g(x float64) float64 {
	//keluaran dari fungsi g
	return x - 2
}

func h(x float64) float64 {
	//keluaran dari fungsi h
	return x + 1
}

//{I.S. Terdefinisi sebuah bilangan asli x
//F.S. y berisi hasil dari fungsi komposisi (𝑓𝑜𝑔𝑜ℎ)(𝑥) }
func komposisi(x float64) {
	//deklarasi variable
	var A, B, C float64

	//gunakan fungsi f, g, dan h lalu masukkan ke variable
	A = h(x)
	B = g(A)
	C = f(B)

	//output hasil dari f(x), g(x), h(x), dan (fogoh)(x)
	fmt.Print("f(", x, ") = ", f(x), "\n")
	fmt.Print("g(", x, ") = ", g(x), "\n")
	fmt.Print("h(", x, ") = ", h(x), "\n")
	fmt.Print("(fogoh)(", x, ") = ", C, "\n")
}

//main program
func main() {
	//deklarasi variable
	var x float64

	//input bilangan
	fmt.Scanln(&x)

	//jalankan procedure komposisi()
	komposisi(x)
}

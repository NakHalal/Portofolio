package main

import (
	"fmt"
)

//procedure findFactorial(in n: integer, in/out result : integer)
//{I.S. Terdefinisi bilangan bulat asli n, n >= 0
//F.S. result berisi hasil dari n!}
func findFactorial(z int) int {
	//deklarasi variable
	var hasil int
	var i int

	//set variable ke angka yang sesuai
	hasil = 1
	i = 1

	//percabangan untuk proses faktorial
	if z < 0 {
		fmt.Print("Faktorial dari bilangan negatif tidak ada.")
	} else {
		for i <= z {
			hasil = hasil * i
			i++
		}
	}

	//keluaran dari fungsi findFactorial
	return hasil
}

//function permutation(n,r : integer) -> integer
//{Mengembalikan hasil n permutasi r, di mana n >= r}
func permutation(n int, r int) int {
	//keluaran dari fungsi permutation
	return (findFactorial(n) / findFactorial(n-r))
}

//function combination(n,r : integer) -> integer
//{Mengembalikan hasil n kombinasi r, di mana n >= r}
func combination(n int, r int) int {
	//keluaran dari fungsi combination
	return (findFactorial(n) / (findFactorial(r) * findFactorial(n-r)))
}

//main program
func main() {
	//deklarasi variable
	var bil1, bil2 int

	//input bilangan 1 dan bilangan 2
	fmt.Scan(&bil1, &bil2)

	//output hasil
	fmt.Print(permutation(bil1, bil2), combination(bil1, bil2))
}

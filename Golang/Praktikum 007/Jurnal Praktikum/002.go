package main

import "fmt"

//deklarasi variable
var total, usaha, nDoa int
var doaOrtu bool
var nilai string

//procedure pengambilan input dan memasukkan ke variable
func BacaData() {
	fmt.Print("Banyaknya usaha? ")
	fmt.Scan(&usaha)
	fmt.Print("Banyaknya doa? ")
	fmt.Scan(&nDoa)
	fmt.Print("Doa orang tua? ")
	fmt.Scan(&doaOrtu)
	fmt.Print("Nilai Algoritma? ")
	fmt.Scan(&nilai)
}

//procedure memasukkan jumlah usaha dan total doa ke variable total
func TabungUsahaDoa(usaha int, nDoa int) {
	total = usaha + nDoa
}

//fungsi mengalikan total dua kali jika doaOrtu == True
func TabungDoaOrtu(doa bool, total int) int {
	if doa {
		return total * 2
	} else {
		return total
	}
}

//procedure pengurangan variabel total dengan nilai yang didapatkan
func HasilNilaiAlpro(nilai string) {
	if nilai == "A" {
		total = total - 150
	} else if nilai == "B" {
		total = total - 130
	} else if nilai == "C" {
		total = total - 100
	}
}

//fungsi untuk menentukan keluaran kelulusan
func HasilAkhir(poin int) string {
	if poin >= 130 {
		return "Lulus langsung dapat kerja gaji 2 digit"
	} else if poin >= 50 && poin < 130 {
		return "Lulus langsung dapat kerja"
	} else {
		return "Jangan lelah berdoa dan berusaha, tidak ada yang sia – sia dari usaha dan doa"
	}
}

//program utama
func main() {
	total = 0
	BacaData()
	//BacaData(usaha, nDoa, doaOrtu, nilai)
	TabungUsahaDoa(usaha, nDoa)
	//fmt.Print(total)
	total = TabungDoaOrtu(doaOrtu, total)
	//fmt.Print(total)
	HasilNilaiAlpro(nilai)
	//fmt.Print(total)
	fmt.Print(HasilAkhir(total))
}

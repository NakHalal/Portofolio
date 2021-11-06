package main

import "fmt"

var jumlahHari, ygDitanggung, jumlahMhs, biaya, totalBiaya int
var tujuan string

func tanggungganHari(jumlahHari int, tujuan string) int {
	if jumlahHari > 3 && tujuan == "domestik" {
		return 3
	} else if jumlahHari > 8 && tujuan == "mancanegara" {
		return 8
	} else {
		return jumlahHari
	}
}

func biayaPerhari(jumlahMhs int) int {
	return ((350 + 2500 + 3000) * jumlahMhs)
}

func perhitunganBiaya(jumlahMhs int, jumlahHari int, tujuan string) {
	ygDitanggung = tanggungganHari(jumlahHari, tujuan)
	biaya = biayaPerhari(jumlahMhs)
	if tujuan == "mancanegara" {
		biaya = biaya * 15 / 10
	}
	totalBiaya = (biaya * ygDitanggung)
}

func main() {
	fmt.Scan(&jumlahMhs, &jumlahHari, &tujuan)
	perhitunganBiaya(jumlahMhs, jumlahHari, tujuan)
	fmt.Print(totalBiaya)
}

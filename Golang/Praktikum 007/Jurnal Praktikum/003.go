package main

import "fmt"

//deklarasi variable
var tgl1, bln1, thn1, tgl2, bln2, thn2 int
var tanggal1, tanggal2, tahun1, tahun2 int
var hari, bulan1, bulan2 string

//fungsi pengecekan tahun kabisat atau tidak
func Kabisat(tahun int) bool {
	return (tahun%400 == 0 || tahun%4 == 0 && tahun%100 != 0)
}

//fungsi mengubah bulan ke angka
func Bulan2Angka(bulan string) int {
	if bulan == "januari" {
		return 1
	} else if bulan == "februari" {
		return 2
	} else if bulan == "maret" {
		return 3
	} else if bulan == "april" {
		return 4
	} else if bulan == "mei" {
		return 5
	} else if bulan == "juni" {
		return 6
	} else if bulan == "juli" {
		return 7
	} else if bulan == "agustus" {
		return 8
	} else if bulan == "september" {
		return 9
	} else if bulan == "oktober" {
		return 10
	} else if bulan == "november" {
		return 11
	} else {
		return 12
	}
}

//fungsi mengubah angka ke bulan
func Angka2Bulan(angka int) string {
	if angka == 1 {
		return "januari"
	} else if angka == 2 {
		return "februari"
	} else if angka == 3 {
		return "maret"
	} else if angka == 4 {
		return "april"
	} else if angka == 5 {
		return "mei"
	} else if angka == 6 {
		return "juni"
	} else if angka == 7 {
		return "juli"
	} else if angka == 8 {
		return "agustus"
	} else if angka == 9 {
		return "september"
	} else if angka == 10 {
		return "oktober"
	} else if angka == 11 {
		return "november"
	} else {
		return "desember"
	}
}

//fungsi untuk menentukan jumlah hari dalam bulan tertentu
func JumlahHari(bln int, thn int) int {
	if bln == 1 || bln == 3 || bln == 5 || bln == 7 || bln == 8 || bln == 10 || bln == 12 {
		return 31
	} else if bln == 4 || bln == 6 || bln == 9 || bln == 11 {
		return 30
	} else {
		if Kabisat(thn) {
			return 29
		} else {
			return 28
		}
	}
}

//procedure untuk menentukan kapan tanggal pengambilan visa
func Pengambilan(tgl1 int, bln1 int, thn1 int, hari string) {
	var waktu_proses, totalHari int
	if hari == "kamis" || hari == "jumat" {
		waktu_proses = 4
	} else {
		waktu_proses = 2
	}
	tgl2 = tgl1 + waktu_proses
	bln2 = bln1
	//{mencari lama hari dalam bulan tersebut}
	totalHari = JumlahHari(bln1, thn1)
	//{masih di bulan yang sama}
	if tgl2 <= totalHari {
		bln2 = bln1
		thn2 = thn1
	} else {
		//{ganti bulan, mungkin ganti tahun juga}
		tgl2 = tgl2 - totalHari
		if bln2 == 12 {
			//{ganti bulan dan tahun}
			bln2 = 1
			thn2 = thn1 + 1
		} else {
			//{hanya ganti bulan saja}
			bln2 = bln2 + 1
			thn2 = thn1
		}
	}
}

//program utama
func main() {
	//{lakukan pembacaan masukan di sini}
	fmt.Scan(&tanggal1, &bulan1, &tahun1, &hari)
	//{panggil subprogram untuk penentuan tanggal pengambilan}
	bln1 = Bulan2Angka(bulan1)
	Pengambilan(tanggal1, bln1, tahun1, hari)
	//{tampilkan tanggal pengambilan visa}
	bulan2 = Angka2Bulan(bln2)
	fmt.Print(tgl2, " ", bulan2, " ", thn2)
}

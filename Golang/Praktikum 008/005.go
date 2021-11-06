package main

import (
	"fmt"
)

var soal, soaltemp int
var totwaktu, totwaktutemp int

//var skor, menit int
var menit int
var nama, namatemp string

func hitungSkor(soal *int, totwaktu *int) {
	var i int
	i = 0
	for i < 8 {
		fmt.Scan(&menit)
		if menit <= 300 && menit != 0 {
			//skor += menit
			*soal += 1
			*totwaktu += menit
		}
		i += 1
	}
}

func main() {
	for nama != "Selesai" {
		namatemp = nama
		fmt.Scan(&nama)
		if nama == "Selesai" {
			nama = namatemp
			break
		}
		totwaktutemp = totwaktu
		totwaktu = 0
		soaltemp = soal
		soal = 0
		hitungSkor(&soal, &totwaktu)
		if soaltemp == soal {
			if totwaktutemp < totwaktu {
				totwaktu = totwaktutemp
				nama = namatemp
			}
		} else if soaltemp > soal {
			soal = soaltemp
			nama = namatemp
			totwaktu = totwaktutemp
		}
	}
	fmt.Print(nama, " ", soal, " ", totwaktu, "\n")
}

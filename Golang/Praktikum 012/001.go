package main

import (
	"fmt"
	"math"
)

const NMAX = 100

type Provinsi struct {
	nama     string
	populasi int
	tumbuh   float64
}

type DataProvinsi struct {
	tabel     [NMAX]Provinsi
	nProvinsi int
}

func main() {
	fmt.Print("Masukkan Data Pertumbuhan Provinsi: \n")
	var BAK Provinsi

	var TAB DataProvinsi

	var i int = 0
	for BAK.nama != "NONE" || BAK.populasi != 0 || BAK.tumbuh != 0.0 {
		fmt.Scan(&BAK.nama, &BAK.populasi, &BAK.tumbuh)
		TAB.tabel[i] = BAK
		TAB.nProvinsi = i
		i++
	}

	fmt.Print("Nama Provinsi? ")
	var BTK string
	fmt.Scan(&BTK)

	BAK = cariProvinsi(TAB, BTK)
	fmt.Print(BAK.nama, " ", BAK.populasi, " ", BAK.tumbuh, "\n")

	fmt.Print("Prediksi populasi tahun depan provinsi? ")
	fmt.Scan(&BTK)

	fmt.Print(prediksi(TAB, BTK), "\n")

	fmt.Print("Urutan data pertumbuhan provinsi berdasarkan populasi terurut menurun: \n")
	urutData(&TAB)

	for X := 0; X < TAB.nProvinsi; X++ {
		fmt.Print(TAB.tabel[X].nama, " ", TAB.tabel[X].populasi, " ", TAB.tabel[X].tumbuh, "\n")
	}
}

func cariProvinsi(data DataProvinsi, nama string) Provinsi {
	//{Terdefinisi data yang sudah terisi dan nama provinsi yang dicari.
	//Fungsi melakukan sequential search dan mengembalikan Provinsi dengan nama yang sesuai}
	var RTHIS int = -1
	for i := 0; i < data.nProvinsi; i++ {
		if data.tabel[i].nama == nama {
			RTHIS = i
		}
	}
	return data.tabel[RTHIS]
}

func prediksi(data DataProvinsi, nama string) int {
	//{Terdefinisi data yang sudah terisi dan nama provinsi yang diprediksi.
	//Fungsi menghitung prediksi populasi tahun berikutnya dan mengembalikannya}
	var WHERE Provinsi = cariProvinsi(data, nama)

	return int(math.Ceil(float64(WHERE.populasi)*float64(WHERE.tumbuh) + float64(WHERE.populasi)))
}

func urutData(data *DataProvinsi) {
	/* {I.S. Terdefinisi data yang sudah terisi
	Proses: mengurutkan data berdasarkan populasi descending dengan selection sort/insertion sort
	F.S. data sudah terurut} */
	for i := 1; i < data.nProvinsi; i++ {
		var j int = i
		for j > 0 {
			if data.tabel[j-1].populasi < data.tabel[j].populasi {
				data.tabel[j-1], data.tabel[j] = data.tabel[j], data.tabel[j-1]
			}
			j--
		}
	}
}

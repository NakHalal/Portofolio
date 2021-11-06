package main

import "fmt"

const NMAX = 1000000

// tipe bentukan partai
type Partai struct {
	NomorPartai int
	Skor        int
}

// tipe array of partai dengan kapasitas NMAX
var TAB [NMAX]Partai

func Posisi(TAB *[NMAX]Partai, N int, NAMA int) int {
	/* 	mengembalikan indeks partai yang memiliki nama yang dicari pada array t yang berisi
	n partai atau -1 apabila tidak ditemukan , gunakan pencarian sekuensial */
	var This int = -1
	for i := 0; i < N; i++ {
		if NAMA == TAB[i].NomorPartai {
			This = i
		}
	}
	return This
}

func main() {
	// deklarasi variabel
	var P [NMAX]int
	var X int
	var TotalSuara int = 0

	X = 1
	// lakukan proses input suara secara berulang di sini, simpan ke dalam array p,
	// sehingga terdapat array p yang berisi hasil peroleh suara n partai.
	i := 0
	for X > 0 {
		fmt.Scan(&X)
		if X > 0 {
			P[i] = X
			TotalSuara++
			i++
		}
	}

	j := 0
	k := 0
	for j < TotalSuara {
		if Posisi(&TAB, TotalSuara, P[j]) == -1 {
			TAB[k].NomorPartai = P[j]
			TAB[k].Skor += 1
			k++
		} else {
			TAB[Posisi(&TAB, TotalSuara, P[j])].Skor += 1
		}
		j++
	}

	// lakukan proses pengurutan dengan insertion sort descending berdasarkan jumlah suara yang diperoleh
	for l := 1; l < TotalSuara; l++ {
		m := l
		for m > 0 {
			if TAB[m-1].Skor < TAB[m].Skor {
				TAB[m-1], TAB[m] = TAB[m], TAB[m-1]
			}
			m = m - 1
		}
	}
	// tampilkan array p
	for o := 0; o < k; o++ {
		fmt.Print(TAB[o].NomorPartai, "(", TAB[o].Skor, ") ")
	}
}

package main

import "fmt"

const NMAX = 100

type belanja [NMAX]int

func main() {
	// Deklarasi Variabel
	var t belanja
	var n, ha int
	var hp float64
	// Lakukan proses masukan
	n = 0
	entri(&t, &n)
	// Hitung total belanja
	ha = total(t, n)
	// tentukan apakah mendapatkan promo atau tidak
	if ha > 100000 {
		// lakukan pengurutan
		urut(&t, n)
		// lakukan perhitungan promo
		promo(t, n, &hp)
		// tampilkan keluaran yang diminta
		fmt.Println(ha, hp)
	} else {
		// tampilkan keluaran yang diminta
		fmt.Println(ha, ha)
	}
}

func entri(t *belanja, n *int) {
	/* IS. data belanja telah siap pada piranti masukan
	FS. array t berisi sejumlah n harga barang yang dibeli */
	var harga, jumlah int = -1, -1

	for i := 0; i < NMAX && harga != 0 && jumlah != 0; i++ {
		fmt.Scan(&harga, &jumlah)
		if harga != 0 && jumlah != 0 {
			*n = *n + 1
			t[i] = harga * jumlah
		}
	}
}

func urut(t *belanja, n int) {
	/* IS. terdefinisi array t yang berisi n harga barang yang dibeli
	FS. array t terurut secara ascending berdasarkan harga barang dengan selection/insertion sort */
	for i := 1; i < n; i++ {
		var j int = i
		for j > 0 {
			if t[j-1] > t[j] {
				t[j-1], t[j] = t[j], t[j-1]
			}
			j--
		}
	}
}

func total(t belanja, n int) int {
	/* IS. terdefinisi array t yang berisi n harga barang yang dibeli
	FS. mengembalikan total harga barang yang terdapat pada array t */
	var i, total int
	i = 0
	total = 0
	for i < n {
		total = t[i] + total
		i++
	}
	return total
}

func promo(t belanja, n int, hp *float64) {
	/* IS. terdefinisi array t yang berisi n harga barang yang dibeli dan terurut ascending
	FS. hp berisi total harga setiap barang setelah dikurangi dengan diskonnya*/
	var i int
	var diskon float64

	*hp = 0
	i = 0

	total := 0
	for j := 0; j < n; j++ {
		total += t[j]
	}
	*hp = float64(total)
	for i < n {
		diskon = Percent(i+1, t[i])
		*hp = *hp - diskon
		i++
	}
}

func Percent(percent int, all int) float64 {
	return ((float64(all) * float64(percent)) / float64(100))
}

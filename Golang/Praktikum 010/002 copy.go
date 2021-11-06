package main

import "fmt"

const nmax = 107

type array = [nmax]string

func posisi(tab array, n int, x string) int {
	/*mengembalikan indeks dari x pada array tab,
	apabila x ditemukan di dalam tab yang berisi n buah nilai,
	-1 apabila tidak ditemukan*/
	var idx int
	for i := 0; i < n; i++ {
		if tab[i] == x {
			idx = i
		}
	}
	if idx == 0 {
		if tab[idx] != x {
			idx = -1
		}
	}
	return idx
}

func hapus(tab *array, n *int, x string) {
	/*IS. terdefinisi sebuah array tab yang berisi n buah nim mahasiswa,
	dan x adalah nim mahasiswa yang wisuda
	FS. apabila x ditemukan pada tab, maka nim dihapus, seluruh elemen setelahnya bergeser,
	dan n berkurang 1. tab dan n tidak berubah apabila x tidak di temukan*/
	var idx int
	var temp [nmax]string

	idx = posisi(*tab, *n, x)

	if idx == 0 {
		for i := 0; i < *n; i++ {
			temp[i] = tab[i+1]
		}
		*n--
		*tab = temp
	} else if idx == (*n - 1) {
		for i := 0; i < (*n - 1); i++ {
			temp[i] = tab[i]
		}
		*n--
		*tab = temp
	} else if idx > 0 && idx < *n {
		for i := 0; i < idx; i++ {
			temp[i] = tab[i]
		}
		for i := idx + 1; i < *n; i++ {
			temp[i-1] = tab[i]
		}
		*n--
		*tab = temp
	}
}
func updateKelulusan(mhs *array, wisuda *array, n *int, m int) {
	/* IS. terdefinisi array mhs dan wisuda yang berisi sejumlah n dan m nim mahasiswa
	FS. seluruh nim mahasiswa wisuda dihapus dari array mhs, nilai n terupdate */
	for i := 0; i < *n; i++ {
		for j := 0; j < m; j++ {
			if mhs[i] == wisuda[j] {
				hapus(mhs, n, wisuda[j])
				i = 0
				j = 0
			}
		}
	}
}
func main() {
	var n, m int
	var daftar, wisuda [nmax]string
	var nimwisuda, nimsudahwisuda string

	// lakukan proses input untuk baris pertama
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&nimwisuda)
		daftar[i] = nimwisuda
	}

	// lakukan proses input untuk baris kedua
	fmt.Scan(&m)
	for i := 0; i < m; i++ {
		fmt.Scan(&nimsudahwisuda)
		wisuda[i] = nimsudahwisuda
	}

	// panggil prosedur update kelulusan di sini
	updateKelulusan(&daftar, &wisuda, &n, m)

	// lakukan proses output array daftar di sini
	fmt.Print(n, " ")
	for i := 0; i < n; i++ {
		fmt.Print(daftar[i], " ")
	}
}

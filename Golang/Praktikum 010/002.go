package main

import "fmt"

const nmax = 107

type array = [nmax]string

func posisi(tab array, n int, x string) int {
	/*mengembalikan indeks dari x pada array tab,
	apabila x ditemukan di dalam tab yang berisi n buah nilai,
	-1 apabila tidak ditemukan*/
	var index int = -1
	i := 0
	for i < n {
		if tab[i] == x {
			index = i
		}
		i++
	}
	return index
}

func hapus(tab *array, n *int, x string) {
	/*IS. terdefinisi sebuah array tab yang berisi n buah nim mahasiswa,
	dan x adalah nim mahasiswa yang wisuda
	FS. apabila x ditemukan pada tab, maka nim dihapus, seluruh elemen setelahnya bergeser,
	dan n berkurang 1. tab dan n tidak berubah apabila x tidak di temukan*/
	var index int
	var temp [nmax]string

	index = posisi(*tab, *n, x)

	if index == 0 {
		i := 0
		for i < *n {
			temp[i] = tab[i+1]
			i++
		}
		*n--
		*tab = temp
	} else if index == (*n - 1) {
		i := 0
		for i < (*n - 1) {
			temp[i] = tab[i]
			i++
		}
		*n--
		*tab = temp
	} else if index > 0 && index < *n {
		i := 0
		for i < index {
			temp[i] = tab[i]
			i++
		}
		i = index + 1
		for i < *n {
			temp[i-1] = tab[i]
			i++
		}
		*n--
		*tab = temp
	}
}
func updateKelulusan(mhs *array, wisuda *array, n *int, m int) {
	/* IS. terdefinisi array mhs dan wisuda yang berisi sejumlah n dan m nim mahasiswa
	FS. seluruh nim mahasiswa wisuda dihapus dari array mhs, nilai n terupdate */
	i := 0
	for i < *n {
		j := 0
		for j < m {
			if mhs[i] == wisuda[j] {
				hapus(mhs, n, wisuda[j])
				i = 0
				j = 0
			}
			j++
		}
		i++
	}
}
func main() {
	var n, m, i int
	var daftar, wisuda array
	var nimwisuda, nimsudahwisuda string

	// lakukan proses input untuk baris pertama
	fmt.Scan(&n)
	i = 0
	for i < n {
		fmt.Scan(&nimwisuda)
		daftar[i] = nimwisuda
		i++
	}

	// lakukan proses input untuk baris kedua
	fmt.Scan(&m)
	i = 0
	for i < m {
		fmt.Scan(&nimsudahwisuda)
		wisuda[i] = nimsudahwisuda
		i++
	}

	// panggil prosedur update kelulusan di sini
	updateKelulusan(&daftar, &wisuda, &n, m)

	// lakukan proses output array daftar di sini
	fmt.Print(n, " ")
	i = 0
	for i < n {
		fmt.Print(daftar[i], " ")
		i++
	}
}

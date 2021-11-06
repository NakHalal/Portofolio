package main
import "fmt"

const NMAX = 100

type mahasiswa struct{
	nama string
	tinggi int
}

type dataMhs [NMAX]mahasiswa

func main(){
	var newTabel dataMhs
	var n int


	fmt.Scanln(&n)
	bacaData(&newTabel, &n)
	urutData(&newTabel, n)
	cetakData(newTabel, n)
}

func bacaData(t *dataMhs, n *int) {
/* IS. n data mahasiswa telah siap pada piranti masukan
FS. menerima input n dan array t berisi n data tinggi mahasiswa */
	var i, masukantinggi int
	var masukannama string

	fmt.Scanln(&masukannama, &masukantinggi)
	i = 0
	for i < *n {
		t[i].nama = masukannama
		t[i].tinggi = masukantinggi
		fmt.Scanln(&masukannama, &masukantinggi)
		i++
	}

}

func cetakData(t dataMhs, n int) {
/* IS. terdefinisi sebuah array t yang berisi n data tinggi mahasiswa
FS. menampilkan array t ke layar monitor */
	var i int

	for i < n {
		fmt.Println(t.[i])
		i++
	}
}

func urutData(t *dataMhs, n int){
/* IS. terdefinisi sebuah array t yang berisi n data tinggi mahasiswa
FS. array t terurut ascending berdasarkan tinggi dengan algoritma selection sort
*/
	var pass, idx, i int
	var temp mahasiswa

	pass = 1
	for pass <= (n-1) {
		idx = pass - 1
		i = pass
		while i < n {
			if *t[idx].tinggi < *t[i].tinggi {
				idx = i
			}
			i++
		}
		temp = *t[pass-1]
		t.[pass-1] = *t[idx]
		t.[idx] = temp
		pass = pass + 1
	}
}
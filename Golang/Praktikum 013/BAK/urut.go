package main
import "fmt"

func main(){
	var tabel [100]int
	var n, u, d int

	fmt.Scanln(&n, &d, &u)
	isiArray(&tabel, &n)
	sorting(&tabel, u, d, n)
	tampilArray(tabel, n)

}

func isiArray(t *[100]int, n *int){
/* IS. terdefinisi bilangan bulat n, dan n buah bilangan bulat telah siap pada piranti masukan
FS. array t berisi n buah bilangan bulat yang berasal dari user */
	var i, input int

	i = 0
	for i < *n {
		fmt.Scan(&input)
		t[i] = input
		i++
	}
}

func tampilArray(t [100]int, n int){
/* IS. terdefinisi sebuah array t yang berisi n buah bilang bulat
FS. menampilkan array t ke layar secara horizontal */
	var i int

	i = 0

	for i < n {
		fmt.Print(t[i], " ")
		i++
	}
}

func sorting(t *[100]int, u,d,n int){
/* IS. terdefinisi sebuah array t yang berisi n bilangan bulat, dan indeks bilangan bulat u dan d
FS. array t terurut descending dari indeks ke-d hingga ke-u dengan menggunakan algoritma insertion sort */
	var i, temp int

	j = d + 1
	for j < u {
		i = j - 1
		k = j
		for k > d {
			if t[i] < t[k] {
				temp = t[k]
				t[k] = t[i]
				t[i] = temp
			}
			y--
		}
		j++
	}
	

}
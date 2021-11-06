package main 
import "fmt"

const NMAX = 100
type belanja [NMAX]int


func main(){
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
	if ha > 100000{
		// lakukan pengurutan
		urut(&t, n)
		// lakukan perhitungan promo
		promo(t, n, &hp)
		// tampilkan keluaran yang diminta 
		fmt.Println(ha,hp)
	}else{
		// tampilkan keluaran yang diminta 
		fmt.Println(ha,ha)
	}
}

func entri(t1 *belanja, n *int){
	/* IS. data belanja telah siap pada piranti masukan
	FS. array t berisi sejumlah n harga barang yang dibeli */
	var i int

	fmt.Scan(&harga, &jumlah)
	for i < NMAX && harga != 0 && jumlah != 0 {
		t1[i] = harga * jumlah
		*n = *n + 1
		fmt.Scan(&harga, &jumlah)
		i++
	}
}
	
func urut(t *belanja, n int){
	/* IS. terdefinisi array t yang berisi n harga barang yang dibeli
	FS. array t terurut secara ascending berdasarkan harga barang dengan selection/insertion sort */
	var i int

	pass = 1
	//pengururtan dengan selection search
	for pass <= n-1 {
		idx = pass - 1
		i = pass
		for i < n {
			if t[idx] < t[i] {
				idx = i
			}
			i++
		}
		temp = t[pass-1]
		t[pass-1] = t[idx]
		t[idx] = temp
	} 
}

func total(t1 belanja, n int) int {
	/* IS. terdefinisi array t yang berisi n harga barang yang dibeli
	FS. mengembalikan total harga barang yang terdapat pada array t */
	var i int
	i =0
	total = 0
	for i < n {
		total = t1[i]+ total
		i++
	}
	return total
}

func promo(t belanja, n int, hp* float64){
	/* IS. terdefinisi array t yang berisi n harga barang yang dibeli dan terurut ascending
	FS. hp berisi total harga setiap barang setelah dikurangi dengan diskonnya*/
	var i int
	var dsikon float64

	*hp = 0
	i = 0
	for i < n {
		diskon = float64(t[i]) * float64(i+1) / float(100)
		*hp = *hp + float(t[i]) - diskon
		i++
	}
	
}
	
	
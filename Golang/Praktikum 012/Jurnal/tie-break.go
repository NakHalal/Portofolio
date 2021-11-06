package main

const N int = 1001

type attribut struct {
	nama1, nama2 string
	jumGol int
	jumAssist int
}

type pemain [N]attribut

func main() {
	var n int
	var peserta pemain

	fmt.Scanln(&n)

	for i := 0; i <n; i++ {
		fmt.Scan(&peserta[i].nama1)
		fmt.Scan(&peserta[i].nama2)
		fmt.Scan(&peserta[i].jumGol)
		fmt.Scan(&peserta[i].jumAssist)
	}

	for j := 0; j < n ; j++ {
		max := j
		k := j + 1
		for k < n {
			if peserta[k].jumGol > peserta[max].jumGol {
				max = k
			} else if peserta[k].jumGol == peserta[max].jumGol{
				if peserta[k].jumAssist > peserta[max].jumAssist{
					max = k
				}
			}
			k++
		}
		temp[o] = peserta[max]
		peserta[max] = peserta[j]
		peserta[j] = temp[0]

	}
	fmt.Print(" ---Output--- ")
	for i := 0; i < n ; i++ {
		fmt.Println(peserta[i].nama1, " ", peserta[i].nama2," ",peserta[i].jumGol," ", peserta[i].jumAssist)
	}
}
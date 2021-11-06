package main

import (
	"fmt"
	"sort"
)

func main() {
	var Suara []int
	var HaiHai [20]int
	var n, i, j, WinRt, l, TP, Winner int

	n = 1
	i = 0
	l = 0
	for n != 0 {
		fmt.Scan(&n)
		if n > 0 && n < 20 {
			Suara = append(Suara, n)
			//Suara[i] = n
			i += 1
		} else if n == 0 {
			break
		}
		l += 1
	}
	sort.Ints(Suara)
	//fmt.Print(Suara)

	j = 0
	for j < len(Suara) {
		TP = (Suara[j] - 1)
		HaiHai[TP] += 1
		j += 1
	}
	//fmt.Print(HaiHai)

	fmt.Print("Suara Masuk: ", l, "\n")
	fmt.Print("Suara Sah: ", i, "\n")

	/*
		k = 0
		for k < len(HaiHai) {
			if HaiHai[k] != 0 {
				fmt.Print(k+1, ": ", HaiHai[k], "\n")
			}
			k += 1
		}
	*/

	WinRt = 0
	Winner = -1
	for WinRt <= 19 {
		//fmt.Println(HaiHai[WinRt])
		if Winner < HaiHai[WinRt] {
			Winner = WinRt + 1
		}
		WinRt++
	}
	fmt.Print("Ketua RT: ", Winner, "\n")

	/*
		fmt.Println(HaiHai)
		fmt.Println(Suara)
	*/

	HaiHai[Winner-1] = 0
	WinRt = 0
	Winner = -1
	for WinRt <= 19 {
		//fmt.Println(HaiHai[WinRt])
		if Winner < HaiHai[WinRt] {
			Winner = WinRt + 1
		}
		WinRt++
	}
	fmt.Print("Wakil Ketua: ", Winner, "\n")

}

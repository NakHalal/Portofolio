package main

import (
	"fmt"
	"sort"
)

func main() {
	var Vote []int
	var Nilai [20]int
	var n, i, j, l, TEMP int = -1, 0, 0, 0, 0

	for n != 0 {
		fmt.Scan(&n)
		if n > 0 && n < 20 {
			Vote = append(Vote, n)
			i += 1
		} else if n == 0 {
			break
		}
		l += 1
	}
	sort.Ints(Vote)

	for j < len(Vote) {
		TEMP = (Vote[j] - 1)
		Nilai[TEMP] += 1
		j += 1
	}

	fmt.Print("Vote Masuk: ", l, "\n")
	fmt.Print("Vote Sah: ", i, "\n")

	/*
		for k < len(Nilai) {
			if Nilai[k] != 0 {
				fmt.Print(k+1, ": ", Nilai[k], "\n")
			}
			k += 1
		}
	*/

	WinRT := 0
	Winner := -1
	for WinRT <= (len(Nilai) - 1) {
		//fmt.Print(Nilai[WinRT])
		if Winner < Nilai[WinRT] {
			Winner = WinRT + 1
		}
		WinRT++
	}
	fmt.Print("Ketua RT: ", Winner, "\n")

	Nilai[Winner-1] = 0
	WinRT = 0
	Winner = -1
	for WinRT <= (len(Nilai) - 1) {
		//fmt.Print(Nilai[WinRT])
		if Winner < Nilai[WinRT] {
			Winner = WinRT + 1
		}
		WinRT++
	}
	fmt.Print("Wakil Ketua: ", Winner, "\n")
}

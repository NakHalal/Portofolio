package main

import (
	"fmt"
)

func main() {
	var winner, player, temp string
	var A, B int
	var i, ronde int
	var nilai, answer int

	winner = "A"
	player = "B"
	_ = A
	_ = B
	ronde = 1
	fmt.Print("Ronde ", ronde, ":\n")
	fmt.Print(winner, " masukkan angka rahasia: ")
	fmt.Scan(&nilai)
	for nilai != -101 {
		i = 1
		fmt.Print(player, " - masukkan angka tebakan ke-", i, ": ")
		fmt.Scan(&answer)
		for i < 3 && answer != nilai {
			i = i + 1
			fmt.Print(player, " - masukkan angka tebakan ke-", i, ": ")
			fmt.Scan(&answer)
		}
		if nilai == answer {
			temp = winner
			winner = player
			player = temp
		}
		print(winner, " adalah pemenagnya\n\n")
		ronde = ronde + 1
		fmt.Print("Ronde ", ronde, ":\n")
		fmt.Print(winner, " - masukkan angka rahasia: ")
		fmt.Scan(&nilai)
	}
	fmt.Print("Permainan selesai\n")
}

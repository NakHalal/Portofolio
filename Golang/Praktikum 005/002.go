package main

import (
	"fmt"
)

func main() {
	var i, n, bobot, sks int
	var nilai string
	var jum_sks, jum int

	fmt.Scan(&n)
	jum = 0
	jum_sks = 0
	i = 1
	for i <= n {
		fmt.Scan(&nilai, &sks)
		for !(sks > 0 && (nilai == "A" || nilai == "B" || nilai == "C" || nilai == "D" || nilai == "E")) {
			fmt.Scan(&nilai, &sks)
		}
		if nilai == "A" {
			bobot = 4
		} else if nilai == "B" {
			bobot = 3
		} else if nilai == "C" {
			bobot = 2
		} else if nilai == "D" {
			bobot = 1
		} else {
			bobot = 0
		}
		jum = jum + bobot*sks
		jum_sks = jum_sks + sks
		i = i + 1
	}
	fmt.Print(jum / jum_sks)
}

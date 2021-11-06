package main

import "fmt"

const NMAX int = 1000

type Scoreboard struct {
	FName  string
	LName  string
	Goal   int
	Assist int
}

func SortThis(items *[NMAX]Scoreboard, n int) {
	//var n = len(items)
	for i := 1; i < n; i++ {
		j := i
		for j > 0 {
			if items[j-1].Goal < items[j].Goal {
				items[j-1], items[j] = items[j], items[j-1]
			} else if items[j-1].Goal == items[j].Goal {
				if items[j-1].Assist < items[j].Assist {
					items[j-1], items[j] = items[j], items[j-1]
				}
			}
			j = j - 1
		}
	}
}

func main() {
	var JumlahTim int
	var FName, LName string
	var Goal, Assist int

	var Tab [NMAX]Scoreboard

	fmt.Scan(&JumlahTim)
	for i := 0; i < JumlahTim; i++ {
		fmt.Scan(&FName, &LName, &Goal, &Assist)
		Tab[i].FName = FName
		Tab[i].LName = LName
		Tab[i].Goal = Goal
		Tab[i].Assist = Assist
	}
	SortThis(&Tab, JumlahTim)

	fmt.Print("\n\n\n———Result: \n")

	for i := 0; i < JumlahTim; i++ {
		fmt.Print(Tab[i].FName, " ", Tab[i].LName, " ", Tab[i].Goal, " ", Tab[i].Assist, "\n")
	}
}

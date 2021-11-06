package main

import "fmt"

type tag struct {
	topik  string
	banyak int
}

func CheckTopic(tabTopic string, tabTag [100]tag) int {
	var result int = -1

	if tabTopic != "" {
		for i := 0; i < 100; i++ {
			if tabTopic == tabTag[i].topik {
				result = i
				break
			} else {
				result = -1
			}
		}
	}

	return result
}

func FillTopic(tabTopic [100]string, tabTag *[100]tag) {
	var Num int = 0

	for i := 0; i < 100; i += 1 {
		if CheckTopic(tabTopic[i], *tabTag) >= 0 {
			tabTag[CheckTopic(tabTopic[i], *tabTag)].banyak += 1
		} else if CheckTopic(tabTopic[i], *tabTag) == -1 {
			tabTag[Num].banyak += 1
			tabTag[Num].topik = tabTopic[i]

			Num += 1
		}
	}
}

func SearchTrend(tabTag [100]tag, TrendingRN *string) {
	var MTopic int = -1

	for i := 0; i < 100; i += 1 {
		if MTopic < tabTag[i].banyak {
			MTopic = tabTag[i].banyak
			*TrendingRN = tabTag[i].topik
		}
	}
}

func main() {
	var tabTopic [100]string
	var tabTag [100]tag
	var TrendingRN string

	for i := 0; i < 100; i += 1 {
		fmt.Scan(&tabTopic[i])
		if tabTopic[i] == "." {
			tabTopic[i] = ""
			break
		}
	}

	FillTopic(tabTopic, &tabTag)
	SearchTrend(tabTag, &TrendingRN)
	fmt.Print(TrendingRN)
}

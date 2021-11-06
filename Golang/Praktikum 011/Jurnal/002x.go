package main

import "fmt"

type tag struct {
	topik  string
	banyak int
}

func cekTopic(tabTopic string, tabTag [100]tag) int {
	var hasil int = -1
	if tabTopic != "" {
		for i := 0; i < 100; i++ {
			if tabTopic == tabTag[i].topik {
				hasil = i
				break
			} else {
				hasil = -1
			}
		}
	}
	return hasil
}

func isiTopic(tabTopic [100]string, tabTag *[100]tag) {
	var valueInput int
	valueInput = 0
	for i := 0; i < 100; i += 1 {
		if cekTopic(tabTopic[i], *tabTag) >= 0 {
			tabTag[cekTopic(tabTopic[i], *tabTag)].banyak += 1

		} else if cekTopic(tabTopic[i], *tabTag) == -1 {
			tabTag[valueInput].topik = tabTopic[i]
			tabTag[valueInput].banyak += 1
			valueInput += 1
		}
	}
}

func trendingTopic(tabTag [100]tag, trendingtopic *string) {
	var mostTopic int
	mostTopic = -1
	for i := 0; i < 100; i += 1 {
		if mostTopic < tabTag[i].banyak {
			mostTopic = tabTag[i].banyak
			*trendingtopic = tabTag[i].topik
		}
	}
}

func main() {
	var tabTopic [100]string
	var tabTag [100]tag
	var trendingtopic string
	for i := 0; i < 100; i += 1 {
		fmt.Scan(&tabTopic[i])
		if tabTopic[i] == "." {
			tabTopic[i] = ""
			break
		}
	}
	isiTopic(tabTopic, &tabTag)
	trendingTopic(tabTag, &trendingtopic)
	fmt.Println(trendingtopic)
}

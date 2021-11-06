package main

import "fmt"

func SearchData(Data [1000]int, SearchThis int) int {
	var Where int = -1
	for i := 0; i < 1000; i++ {
		if Data[i] == SearchThis {
			Where = i
		}
	}

	return Where
}

func CopyData(Data [1000]int, N int, P string, DataKiri *[1000]int, DataKanan *[1000]int, TotalData int, TotalDataKanan *int, TotalDataKiri *int) {
	var Start, End int

	if N == -1 {

	} else if P == "Kiri" {
		Start = 0
		End = N
		for Start <= End {
			DataKiri[Start] = Data[Start]
			Start++
			*TotalDataKiri = End
		}
	} else if P == "Kanan" {
		Start = N
		End = TotalData - 1
		for i := 0; Start <= End; i++ {
			DataKanan[i] = Data[Start]
			Start++
			*TotalDataKanan = i
		}
	}
}

func FindMin(TheData [1000]int, TotalTheData int) int {
	var min = TheData[0]

	for i := 0; i < TotalTheData; i++ {
		if TheData[i] < min {
			min = TheData[i]
		}
	}

	return min
}

func FindMax(TheData [1000]int, TotalTheData int) int {
	var min = TheData[0]

	for i := 0; i < TotalTheData; i++ {
		if TheData[i] > min {
			min = TheData[i]
		}
	}

	return min
}

func main() {
	var N, TotalData, SearchThis int
	var Data, DataKiri, DataKanan [1000]int
	var TotalDataKiri, TotalDataKanan int

	fmt.Scan(&TotalData, &SearchThis)
	for i := 0; i < TotalData; i++ {
		var P int
		fmt.Scan(&P)
		Data[i] = P
	}

	N = SearchData(Data, SearchThis)
	CopyData(Data, N, "Kiri", &DataKiri, &DataKanan, TotalData, &TotalDataKanan, &TotalDataKiri)
	CopyData(Data, N, "Kanan", &DataKiri, &DataKanan, TotalData, &TotalDataKanan, &TotalDataKiri)

	if N == -1 {
		fmt.Print("Tidak Ditemukan!")
	} else {
		fmt.Print(FindMin(DataKiri, TotalDataKiri), " ", FindMax(DataKiri, TotalDataKiri), "\n")
		fmt.Print(FindMin(DataKanan, TotalDataKanan), " ", FindMax(DataKanan, TotalDataKanan), "\n")
	}
}

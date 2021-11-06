package main

import "fmt"

func main() {
	slice := []int{1}
	slice2 := []int{55, 66, 77}
	fmt.Println("Start slice: ", slice[0])
	fmt.Println("Start slice2:", slice2)
	slice = append(slice, 4)
	fmt.Println("Add one item:", len(slice))
}

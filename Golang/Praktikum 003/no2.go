package main

import "fmt"

func main() {
    var angka int
    var a1, a2, a3, a4, a5, a6, a7, a8, a9 int

    fmt.Scanln(&angka)

    a1 = angka / 1000
    a2 = angka / 100 % 10
    a3 = angka % 100 / 10
    a4 = angka % 10
    a5 = angka / 100
    a6 = angka % 1000 / 10
    a7 = angka % 100
    a8 = angka / 10
    a9 = angka % 1000

    fmt.Println(a1)
    fmt.Println(a2)
    fmt.Println(a3)
    fmt.Println(a4)
    fmt.Println(a5)
    fmt.Println(a6)
    fmt.Println(a7)
    fmt.Println(a8)
    fmt.Println(a9)
    fmt.Println(angka)

}
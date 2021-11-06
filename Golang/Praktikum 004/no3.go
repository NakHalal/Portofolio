package main

import "fmt"

func main() {
    var a1, a2, a3, a4, a5 int
    var s1, s2, s3, s4, s5 string
    var quads bool

    fmt.Scanf("%d%s %d%s %d%s %d%s %d%s", &a1, &s1, &a2, &s2, &a3, &s3, &a4, &s4, &a5, &s5)

    fmt.Println(a1, s1, a2, s2, a3, s3, a4, s4, a5, s5)

    //straight = (a1+1 == a2 && a2+1 == a3 && a3+1 == a4 && a4+1 == a5 && a1 != 1) 
    //(a1 == 10 && a2 == 11 && a3 == 12 && a4 == 13 && a5 == 1)

    //flush = s1 == s2 && s2 == s3 && s3 == s4 && s4 == s5

    quads = ((a1 == a2 && a2 == a3 && a3 == a4)  (a2 == a3 && a3 == a4 && a4 == a5)  (a3 == a4 && a4 == a5 && a5 == a1)  (a4 == a5 && a5 == a1 && a1 == a2) || (a5 == a1 && a1 == a2 && a2 == a3))

    fmt.Println(quads)

}
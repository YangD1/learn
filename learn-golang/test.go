package main

import "time"
import "fmt"

var a string

func main() {
  fmt.Println(time.Now())
   a = "G"
   print(a)
   f1()
}

func f1() {
   a := "O"
   print(a)
   f2()
}

func f2() {
   print(a)
}

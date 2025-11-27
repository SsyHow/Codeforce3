package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(x []int, in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	for _, v := range x {
		if b == v {
			Fprintln(out, -1)
			return
		}
	}
	L := make([]int, b)
	for i := 0; i < b; i++ {
		L[i] = i + 1
	}
	for _, v := range x {
		if v < b {
			L[v], L[v-1] = L[v-1], L[v]
		}

	}
	for _, v := range L {
		Fprint(out, v, " ")
	}
	Fprintln(out)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	L := []int{1, 8, 49, 288, 1681, 9800, 57121, 332928}
	for i := 0; i < a; i++ {
		solve(L, in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

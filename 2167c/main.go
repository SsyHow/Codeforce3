package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"slices"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	L := make([]int, b)
	odd, even := false, false
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
		if L[i]&1 == 0 {
			even = true
		} else {
			odd = true
		}
	}
	if odd && even {
		slices.Sort(L)
	}
	for i, v := range L {
		if i > 0 {
			Fprint(out, " ")
		}
		Fprint(out, v)
	}
	Fprintln(out)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b int
	Fscan(in, &a, &b)

	var L []int

	for a > 0 || b > 0 {
		L = append(L, (b%3-a%3+3)%3)
		a /= 3
		b /= 3
	}
	ans := 0
	for len(L) > 0 {
		ans = 3*ans + L[len(L)-1]
		L = L[:len(L)-1]
	}
	Fprintln(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}

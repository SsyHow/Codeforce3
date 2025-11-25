package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b, x int
	Fscan(in, &b)
	L := make([]int, b)
	h := -1 << 60
	l := 1 << 60
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
		h = max(L[i], h)
		l = min(L[i], l)
	}
	Fscan(in, &x)
	if l <= x && x <= h {
		Fprintln(out, "Yes")
	} else {
		Fprintln(out, "No")
	}

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

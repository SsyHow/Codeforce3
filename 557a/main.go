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
	var a, a1, b1, a2, b2, a3, b3 int
	Fscan(in, &a)
	Fscan(in, &a1, &b1, &a2, &b2, &a3, &b3)

	z := a3
	y := a2
	k := a - z - y
	if k == a1 {
		x := a1
		Fprintln(out, x, y, z)
		return
	} else {
		x := min(k, b1)
		y := min(a-x-z, b2)
		z := a - x - y
		Fprintln(out, x, y, z)
		return
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}

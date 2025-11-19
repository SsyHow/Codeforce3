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
	var x, y, a, b int
	Fscan(in, &x, &y, &a, &b)
	type p struct {
		i, j int
	}
	L := make([]p, 0)
	for i := a; i < x+1; i++ {
		for j := b; j < y+1; j++ {
			if i > j {
				L = append(L, p{i, j})
			}
		}
	}
	Fprintln(out, len(L))
	for _, p := range L {
		Fprintln(out, p.i, p.j)
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}

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
	var s, t string
	Fscan(in, &s)
	Fscan(in, &t)
	ss := []rune(s)
	tt := []rune(t)
	n := len(ss)
	L := make([]rune, n)
	f := 0
	for i := 0; i < n; i++ {
		if ss[i] == tt[i] {
			L[i] = ss[i]
		} else {
			if f == 0 {
				L[i] = ss[i]
			} else {
				L[i] = tt[i]
			}
			f = 1 - f
		}
	}
	if f == 1 {
		Fprintln(out, "impossible")
	} else {
		for i := 0; i < n; i++ {
			Fprint(out, string(L[i]), "")
		}

		Fprintln(out)
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}

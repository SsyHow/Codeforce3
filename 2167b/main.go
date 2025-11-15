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
	var s, t string
	Fscan(in, &b)
	Fscan(in, &s, &t)
	L := []rune(s)
	M := []rune(t)
	slices.Sort(L)
	slices.Sort(M)
	k := true
	for i := 0; i < b; i++ {
		if L[i] != M[i] {
			k = false
		}
	}

	if k {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
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

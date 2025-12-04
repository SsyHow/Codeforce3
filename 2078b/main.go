package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n, k int
	Fscan(in, &n, &k)

	L := make([]int, n)
	if k&1 == 1 {
		for i := 0; i < n; i++ {
			L[i] = n
		}
		L[n-1] = n - 1
	} else {
		for i := 0; i < n; i++ {
			L[i] = n - 1
		}
		L[n-2] = n
	}
	for i := 0; i < n; i++ {
		Fprint(out, L[i], " ")
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

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
	for i := 0; i < n; i++ {
		Fscan(in, &L[i])
	}
	ff := true
	x := 0
	for k > 0 {
		i := 0
		f := true
		for i < n-1 {
			if L[i] < L[i+1] {
				L[i] += 1
				x = i
				f = false
				break
			}
			i++
		}

		if f {
			Fprintln(out, -1)
			ff = false
			break
		}
		k--
	}
	if ff {
		Fprintln(out, x+1)
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

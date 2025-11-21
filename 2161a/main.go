package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var r0, x, d, n int
	Fscan(in, &r0, &x, &d, &n)

	var s string
	Fscan(in, &s)
	L := []rune(s)
	ans := 0
	for i := 0; i < n; i++ {
		if L[i] == '2' && r0 >= x {
			continue
		} else {
			r0 = max(0, r0-d)
			ans++
		}
	}
	Fprintln(out, ans)
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

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
	var a int
	Fscan(in, &a)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	l := 0
	h := a - 1
	ans := 0
	for L[h] == L[0] {
		h--
	}
	ans = max(ans, h)

	for L[l] == L[a-1] {
		l++
	}
	ans = max(ans, a-1-l)

	Fprintln(out, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}

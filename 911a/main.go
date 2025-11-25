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
	x := 1 << 60
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
		x = min(x, L[i])
	}
	prev := -1 << 30
	ans := 1 << 30
	for i := 0; i < a; i++ {
		if x == L[i] {
			ans = min(ans, i-prev)
			prev = i
		}
	}
	Fprint(out, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}

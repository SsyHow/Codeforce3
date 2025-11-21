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
	var x int
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
		x = max(x, L[i])
	}

	tmp := 1
	ans := 1
	prev := L[0]

	for i := 1; i < a; i++ {
		if L[i] == prev && prev == x {
			tmp += 1
			ans = max(ans, tmp)
		} else {
			tmp = 1
			prev = L[i]
		}
	}
	Fprint(out, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}

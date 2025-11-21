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
	var b, g, h int
	Fscan(in, &b, &g, &h)
	ans := 0
	for i := 0; i < min(b, h)+1; i++ {
		if h-i <= g {
			ans += 1
		}
	}
	Fprint(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}

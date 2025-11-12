package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b, c int
	var x, y, z int
	Fscan(in, &a, &b, &c)
	Fscan(in, &x, &y, &z)

	if a^x == 1 && b^y == 1 && c^z == 1 {
		Fprintln(out, "NO")
	} else {
		Fprintln(out, "YES")
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}

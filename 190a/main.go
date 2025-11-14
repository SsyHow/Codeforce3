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
	var n, m int
	Fscan(in, &n, &m)
	a := max(n, m)
	b := min(n + max(m-1, 0))

	if n == 0 && m > 0 {
		Fprintln(out, "Impossible")
	} else {
		Fprintln(out, a, b)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

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
	var n, d int
	Fscan(in, &n, &d)
	var a int
	Fscan(in, &a)
	var x, y int
	for i := 0; i < a; i++ {
		Fscan(in, &x, &y)
		if x-d <= y && y <= x+d && d-x <= y && y <= n+(n-d)-x {
			Fprintln(out, "YES")
		} else {
			Fprintln(out, "NO")
		}
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

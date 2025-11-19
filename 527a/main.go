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
	var a, b int
	Fscan(in, &a, &b)

	ans := 0
	for a%b > 0 {
		ans += a / b
		a, b = b, a%b
	}
	ans += a / b
	Fprintln(out, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}

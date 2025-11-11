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
	var n, k int
	Fscan(in, &n, &k)
	f, t := 0, 0
	x := n

	for n%5 == 0 {
		f += 1
		n /= 5
	}
	for n%2 == 0 {
		t += 1
		n /= 2
	}
	ans1 := 1
	ans2 := 1
	f = k - f
	t = k - t
	for f > 0 {
		ans1 *= 5
		f -= 1
	}
	for t > 0 {
		ans2 *= 2
		t -= 1
	}
	Fprintln(out, ans1*ans2*x)
}

func main() {
	run(os.Stdin, os.Stdout)
}

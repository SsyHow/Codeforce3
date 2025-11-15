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
	f := false
	for i := 0; i < a; i++ {
		x := 0
		var b int
		for j := 0; j < a; j++ {
			Fscan(in, &b)
			x = max(x, b)
		}
		if x == a-1 && f {
			x++
		} else if x == a-1 {
			f = true
		}
		Fprint(out, x, " ")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

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
	f := false
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
		if L[i]&1 == 1 {
			f = true
		}
	}
	if f {
		Fprintln(out, "First")
	} else {
		Fprintln(out, "Second")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

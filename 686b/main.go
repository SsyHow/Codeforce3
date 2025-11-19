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

	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	for i := a - 1; i > 0; i-- {
		for j := 0; j < i; j++ {
			if L[j] > L[j+1] {
				L[j], L[j+1] = L[j+1], L[j]
				Fprintln(out, j+1, j+2)
			}
		}
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

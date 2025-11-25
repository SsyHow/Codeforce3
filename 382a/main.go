package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strings"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b string
	Fscan(in, &a, &b)
	part := strings.Split(a, "|")
	p1 := []rune(part[0])
	p2 := []rune(part[1])

	c := []rune(b)

	for i := 0; i < len(c); i++ {
		if len(p1) <= len(p2) {
			p1 = append(p1, c[i])
		} else {
			p2 = append(p2, c[i])
		}

	}
	if len(p1) == len(p2) {
		for i := 0; i < len(p1); i++ {
			Fprint(out, string(p1[i]))
		}
		Fprint(out, "|")
		for i := 0; i < len(p2); i++ {
			Fprint(out, string(p2[i]))
		}
		Fprintln(out)

	} else {
		Fprintln(out, "Impossible")
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}

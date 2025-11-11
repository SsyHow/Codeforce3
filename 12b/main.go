package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"slices"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var s, t string
	Fscan(in, &s, &t)

	ss := []rune(s)
	slices.Sort(ss)
	i := 0
	f := false
	for ss[i] == '0' {
		i += 1
		if i == len(ss) {
			f = true
			break
		}
	}

	if !f {
		ss[0], ss[i] = ss[i], ss[0]
	}
	if string(ss) == t {
		Fprintln(out, "OK")
	} else {
		Fprintln(out, "WRONG_ANSWER")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

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
	var a string
	Fscan(in, &a)
	L := []rune(a)
	s := make(map[rune]int)
	s['0'] = 2
	s['1'] = 7
	s['2'] = 2
	s['3'] = 3
	s['4'] = 3
	s['5'] = 4
	s['6'] = 2
	s['7'] = 5
	s['8'] = 1
	s['9'] = 2
	ans := 1
	for _, v := range L {
		ans *= s[v]
	}
	Fprintln(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}

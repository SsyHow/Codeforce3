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
	var a, b int
	Fscan(in, &a, &b)

	L := make([][]rune, a)
	for i := range L {
		var s string
		Fscan(in, &s)
		L[i] = []rune(s)
	}

	ans := 0
	for i := 0; i < a; i++ {
		for j := 0; j < b; j++ {
			if L[i][j] == 'W' {
				f := false
				if i > 0 && L[i-1][j] == 'P' {
					f = true
				}
				if j > 0 && L[i][j-1] == 'P' {
					f = true
				}
				if i < a-1 && L[i+1][j] == 'P' {
					f = true
				}
				if j < b-1 && L[i][j+1] == 'P' {
					f = true
				}
				if f {
					ans += 1
				}
			}
		}
	}
	Fprintln(out, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}

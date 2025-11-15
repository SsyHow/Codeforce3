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
	var a int
	Fscan(in, &a)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	slices.Sort(L)
	ans := 1 << 60
	cnt := 0
	for i := 0; i < a-1; i++ {
		if L[i+1]-L[i] < ans {
			cnt = 1
			ans = L[i+1] - L[i]
		} else if L[i+1]-L[i] == ans {
			cnt += 1
		}
	}
	Fprintln(out, ans, cnt)

}

func main() {
	run(os.Stdin, os.Stdout)
}

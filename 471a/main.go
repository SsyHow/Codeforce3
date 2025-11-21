package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"slices"
	"sort"
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
	L := make(map[int]int)
	for i := 0; i < 6; i++ {
		Fscan(in, &a)
		L[a] += 1
	}
	K := make([]int, 0)
	for _, v := range L {
		K = append(K, v)
	}
	sort.Ints(K)
	slices.Reverse(K)

	if K[0] == 6 || (K[0] == 4 && K[1] == 2) {
		Fprintln(out, "Elephant")
	} else if K[0] >= 4 && K[1] == 1 {
		Fprintln(out, "Bear")
	} else {
		Fprintln(out, "Alien")
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}

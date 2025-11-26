package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
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

	ans := math.MaxInt
	x := 0
	for i := 1; i < 101; i++ {
		tmp := 0
		for _, j := range L {
			if abs(j-i) > 1 {
				tmp += abs(j-i) - 1
			}
		}
		if tmp < ans {
			ans = tmp
			x = i
		}
	}
	Fprint(out, x, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}

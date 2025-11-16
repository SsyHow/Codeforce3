package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func isPrime(n int64) bool {
	if n < 2 {
		return false
	}
	if n == 2 || n == 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := int64(5); i*i <= n; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func solve(in *bufio.Reader, out *bufio.Writer) {
	var m, n int64
	Fscan(in, &m, &n)

	if isPrime(m+n) && m-n == 1 {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}

}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}

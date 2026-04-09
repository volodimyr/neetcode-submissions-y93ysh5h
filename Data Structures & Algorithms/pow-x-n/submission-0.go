func myPow(x float64, n int) float64 {
    var n1 int
    if n < 0 {
        n1 = -n
    }else {
        n1 = n
    }
    res := pow(x, n1)

    if n < 0 {
        return 1 / res
    }
    return res
}

func pow(x float64, n int) float64 {
    if n == 0 {
        return 1
    }
    return x * pow(x, n-1)
}

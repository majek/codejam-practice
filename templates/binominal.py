
def binominal(n, r):
    p = 1.0
    for i in xrange(r):
        p = p * (n - i) / (i + 1)
    return p

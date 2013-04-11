
import itertools
import math


def binomial_coefficient_naive(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def binomial_coefficient(n, k):
    # via: https://en.wikipedia.org/wiki/Binomial_coefficient
    assert n >= k
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(1, k+1):
        c = c * (n - (k - i))
        c = c // i
    return c

def triangles(line):
    n, A, B, C, D, x0, y0, M = line
    X = x0; Y = y0
    yield (X, Y)
    for _ in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        yield (X, Y)

for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    rems = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    t = list(triangles(map(int, raw_input().split())))
    for x, y in t:
        rems[x % 3][y % 3] += 1

    s = 0
    pairs = [(i,j) for i in range(3) for j in range(3)]
    for a, b in pairs:
        if rems[a][b] > 2:
            s += binomial_coefficient(rems[a][b], 3)

    for (a,b), (c,d), (e,f) in itertools.combinations(pairs, 3):
        if ((a+c+e) % 3 != 0 or
            (b+d+f) % 3 != 0): continue
        s += rems[a][b] * rems[c][d] * rems[e][f]
    print s

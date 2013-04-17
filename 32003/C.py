import sys
from nzmath.combinatorial import binomial

def _sum(d, b):
    r = 0
    j = 0
    while True:
        j += 1
        if j > b:
            break
        v = binomial(d, j)
        r += v
        if r > 4294967296L or v == 0:
            break
    return r

def solve_F(d, b):
    if b == 1 or d == 1:
        # have to go in a sequence
        return d
    if d > b and b > 32:
        return 4294967297L
    # Naively - it's a recursive sequence. But it's pretty slow to
    # count it that way and it consumes the stack
    #  r = solve_F(d - 1, b - 1) + 1 + solve_F(d - 1, b)
    return _sum(d, b)

def guess_first_true(fun):
    i = 1
    while True:
        if fun(i):
            break
        i *= 2

    left = i/2; right = i
    while left+1 != right:
        mid = (left + right) / 2
        if fun(mid):
            right = mid
        else:
            left = mid
    return right


def solve_D(f, b):
    return guess_first_true(lambda i:solve_F(i, b) >= f)

def solve_B(f, d):
    return guess_first_true(lambda i:solve_F(d, i) >= f)


for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    F, D, B = map(long, raw_input().split())

    mem = {}
    mems = {}
    f = solve_F(D, B)
    d = solve_D(F, B)
    b = solve_B(F, D)
    print "%s %s %s" % (f if f < 4294967296 else -1, d, b)

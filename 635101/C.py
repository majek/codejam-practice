import sys


def binominal(n, r):
    p = 1
    for i in xrange(r):
        p = (p * (n - i) / (i + 1))
    return p

def _fun(l, n):
    if l == 1:
        return 1

    ch = n - l - 1
    return sum(fun(ll, l) * binominal(ch, l - ll - 1)
               for ll in xrange(max(1, l-ch-1), l)) % 100003

mem = {}
def fun(l, n):
    k = (l, n)
    if k not in mem:
        mem[k] = _fun(l, n)
    return mem[k]

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()

    print sum(fun(ll, N) for ll in xrange(1, N)) % 100003

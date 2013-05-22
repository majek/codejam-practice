import sys
import random
import bintrees


def solve(a, b):
    k = (a,b)
    if k in mem: return mem[k]

    best = Ellipsis
    for q in Q:
        if q >= a and q < b:
            c = b-a-1 + solve(a, q) + solve(q+1, b)
            best = min(best, c)
    r = mem[k] = best if best != Ellipsis else 0
    return r

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    P, _ = map(int, raw_input().split())
    Q = [int(v)-1 for v in raw_input().split()]

    mem = {}
    print solve(0, P)

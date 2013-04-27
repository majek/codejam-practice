import collections
import itertools
import sys
import math

def solve(e, n):
    k = (e, n)
    if k in mem: return mem[k]

    if n == len(V):
        return 0

    #r = [0 + solve(min(E, e+R), n+1), e*V[n] + solve(R, n+1)]
    r = []
    for s in xrange(0, e+1):
        r.append( s*V[n] + solve(min(E, e-s+R), n+1) )
    mem[k] = max(r)
    return mem[k]

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    E, R, _ = map(int, raw_input().split())
    V = map(int, raw_input().split())

    # gain = v1 * spent

    mem = {}
    print solve(E, 0)

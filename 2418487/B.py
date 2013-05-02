import collections
import itertools
import sys
import math


def suck(n):
    spent = M[n] - T[n]
    S[n] = spent

    s = M[n] - spent
    for r in xrange(n+1, len(M)):
        s += R
        if s >= E:
            break
        if M[r] > s:
            M[r] = s
        else:
            # assert
            break

    s = M[n]
    for r in xrange(n-1, 0-1, -1):
        s -= R
        if s <= 0:
            break
        if T[r] < s:
            # I don't understand that
            T[r] = s

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    E, R, N = map(int, raw_input().split())
    V = map(int, raw_input().split())

    M = [E] * N   # Energy on entry
    T = [0] * N   # Energy reserved, must be available on exit
    S = [0] * N   # Spent

    vp = sorted([(v, p) for p, v in enumerate(V)], reverse=True, key=lambda (a,b):(a, N-b))

    for v, p in vp:
        suck(p)

    print sum(v*p for v,p in itertools.izip(V, S))

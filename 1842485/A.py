import collections
import itertools
import sys
import math
import bisect

sys.setrecursionlimit(20000)


def solve(pos, idx):
    swing = P[idx] - pos

    if idx in mem:
        if mem[idx] >= swing: return False

    if P[idx] + swing >= T:
        return True

    for i in xrange(bisect.bisect_right(P, P[idx] + swing)-1, idx, -1):
        delta = P[i] - P[idx]
        if solve(P[i] - min(delta, S[i]), i):
            return True

    mem[idx] = swing
    return False

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    P = []
    S = []
    for _ in xrange(N):
        p, s = map(int, raw_input().split())
        P.append(p)
        S.append(s)
    T = input()

    mem = {}
    print 'YES' if solve(0, 0) else 'NO'


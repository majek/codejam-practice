import collections
import itertools
import sys
import math


def solve((ta, na), (tb, nb), a, b):
    if a == len(A)-1 or b == len(B)-1:
        return 0

    k = (ta, na, tb, nb, a, b)
    if k in mem: return mem[k]

    resp = [0, 0]
    if ta == tb: # match
        if na < nb:
            resp[0] = na + solve(A[a + 1], (tb, nb-na), a + 1, b)
        else:
            resp[0] = nb + solve((ta, na-nb), B[b + 1], a, b + 1)
    else: # no match
        resp[0] = solve(A[a + 1], (tb, nb), a + 1, b)
        resp[1] = solve((ta, na), B[b + 1], a, b + 1)

    r = mem[k] = max(resp)
    return r


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    raw_input()

    l = map(int, raw_input().split())
    A = zip(l[1::2], l[::2])
    l = map(int, raw_input().split())
    B = zip(l[1::2], l[::2])

    A.append( (None, None) )
    B.append( (None, None) )

    mem = {}
    print solve(A[0], B[0], 0, 0)


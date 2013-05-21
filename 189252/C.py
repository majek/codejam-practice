import sys
import itertools


def cost(Q):
    c = 0
    p = [True] * P
    for v in Q:
        p[v] = None
        for l in xrange(v-1, 0-1, -1):
            if not p[l]:
                break
            c += 1
        for r in xrange(v+1, P):
            if not p[r]:
                break
            c += 1
    return c

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    P, _ = map(int, raw_input().split())
    Q = sorted(int(v)-1 for v in raw_input().split())

    print min(cost(qq) for qq in itertools.permutations(Q))

import sys
from collections import Counter
import bintrees


def cost(o, e, p):
    assert e >= o
    x = e - o
    return (((N-x+N+1)*(x) / 2) * p ) % 1000002013


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())
    K = []
    T = 0
    for _ in xrange(M):
        o, e, p = map(int, raw_input().split())
        T += cost(o, e, p)
        K.append( (o, p) )
        K.append( (e, -p) )

    K.sort(key=lambda (o, p):(o, -p))

    r = bintrees.FastAVLTree()
    C = 0
    for o, p in K:
        if p > 0:
            if o not in r:
                r[o] = 0
            r[o] += p
        else:
            p = -p
            while p:
                oo, pp = r.max_item()
                x = min(pp, p)
                p -= x
                if pp-x:
                    r[oo] = pp-x
                else:
                    del r[oo]
                C += cost(oo, o, x)

    print (T - C) % 1000002013


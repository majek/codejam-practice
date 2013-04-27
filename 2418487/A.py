import collections
import itertools
import sys
import math


def fits(i):
    return ((2*i+1)*(i+1+r) + r) <= t

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    r, t = map(int, raw_input().split())

    lrings = 0
    rrings = 1
    while fits(rrings):
        rrings *= 2
    assert fits(lrings)

    while True:
        m = (lrings + rrings) / 2
        if m == lrings or m == rrings:
            break
        if fits(m):
            lrings = m
        else:
            rrings = m

    print rrings

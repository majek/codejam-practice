import itertools
import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    B = input()
    D = [map(int, raw_input().split()) for _ in xrange(B)]

    h = [(x,y) \
             for x1, y1, x2, y2 in D \
             for x in xrange(x1, x2+1) \
             for y in xrange(y1, y2+1) \
             ]

    cost = lambda a,b: sum(abs(a-x) + abs(b-y) for x,y in h)
    hh = [(cost(x,y), x, y) for x, y in h]
    hh.sort()

    cost, x, y = hh[0]
    print x, y, cost

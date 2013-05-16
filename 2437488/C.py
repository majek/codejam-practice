import collections
import itertools
import sys
import math

from intervaltree import IntervalTree, Interval



for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    attacks = []
    N = input()
    for _ in xrange(N):
        d, n, w, e, s, delta_d, delta_p, delta_s = map(int, raw_input().split())
        for _ in xrange(n):
            attacks.append( (d, s, w, e) )
            d += delta_d
            s += delta_s
            e += delta_p
            w += delta_p


    wall = IntervalTree()

    attacks.sort()
    failed = 0
    for _, g in itertools.groupby(attacks, key=lambda (d,s,w,e): d):
        updates = IntervalTree()
        for _, s, w, e in g:
            here_failed = 0
            for i in wall.fill(Interval(w, e, 0)):
                if i.v < s:
                    here_failed = 1
                    i = Interval(i.a, i.b, s)
                updates.update(i)
            failed += here_failed
        for _, i in updates.t.items():
            wall.update(Interval(i.a, i.b, i.v))
    print failed


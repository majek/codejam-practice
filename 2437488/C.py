import collections
import itertools
import sys
import math




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

    wall = collections.defaultdict(lambda:0)

    attacks.sort()
    all_failed = 0
    for _, g in itertools.groupby(attacks, key=lambda (d,s,w,e): d):
        nwall = wall.copy()
        updates = []
        for d, s, w, e in g:
            failed = False
            for p in xrange(w, e):
                if wall[p] < s:
                    nwall[p] = s
                    failed = True
            #print "d=%r s=%3s p=%s-%s failed=%r" % (d, s, w, e, failed)
            if failed:
                all_failed += 1
        wall = nwall
    print [wall[i] for i in xrange(min(wall.keys()), max(wall.keys())+1)]
    print all_failed


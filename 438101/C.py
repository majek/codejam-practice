import sys
import itertools
import bisect


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    l = map(int, raw_input().split())
    P, C, S = l[0], l[1], l[2:]


    S.sort()

    c = 0
    while True:
        S, R = S[:-C],  [v - 1 for v in S[-C:]]
        if min(R) < 0:
            break
        c += 1
        for v in R:
            idx = bisect.bisect_left(S, v)
            S.insert(idx, v)

    print c


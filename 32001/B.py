import collections
import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M, S2 = map(int, raw_input().split())


    done = False
    for b1 in xrange(1, N+1):
        for b2 in xrange(1, M+1):
            c1_min, _ = divmod(b1*0 - S2, b2)
            c1_max, _ = divmod(b1*M - S2, b2)
            c1_min = max(0, c1_min)
            c1_max = min(c1_max, M+1)
            r = ((S2+c1_min*b2) % b1)
            c1_min += b1- r if r else 0
            for c1 in xrange(c1_min, c1_max+1, b1):
                c2, r = divmod(S2 + c1*b2, b1)
                done = True
                assert S2 == abs(0*b1+b1*c2+c1*0-c1*b2-0*c2-b1*0)
                print "0 0 %s %s %s %s" % (b1, b2, c1, c2)
                break
            if done:
                break
        if done:
            break
    if not done:
        print "IMPOSSIBLE"

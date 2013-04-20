import collections
import itertools
import sys
import math


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),


    N, Pd, Pg = map(int, raw_input().split())

    if Pg == 0 and Pd != 0:
        r = False
    elif Pg == 100 and Pd != 100:
        r = False
    elif Pg == 100 and Pd == 100:
        r = True
    elif Pg == 0 and Pd == 0:
        r = True
    else:
        r = False
        for d in xrange(1, min(100, N)+1):
            x = (d * Pd) / 100.
            if int(x) == x:
                r = True
                break
    print "Possible" if r else "Broken"

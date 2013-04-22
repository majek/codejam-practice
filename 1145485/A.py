import collections
import itertools
import sys
import math
import fractions


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
        x = 100 / fractions.gcd(Pd, 100)
        r = x <= N
    print "Possible" if r else "Broken"


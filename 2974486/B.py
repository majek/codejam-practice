import sys
import itertools

for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),

    C, F, X = map(float, raw_input().split())

    s = 2
    t = 0
    for _ in itertools.count():
        nofab = X / s
        yesfab = C / s + X / (s+F)
        if yesfab < nofab:
            t += C/s
            s += F
        else:
            t += X/s
            break

    print '%0.7f' % t

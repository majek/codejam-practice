import sys

for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    no, src, dst = raw_input().split()

    src = dict((c, v) for v, c in enumerate(src))

    sbase = len(src)
    dbase = len(dst)

    value = 0
    for p, c in enumerate(reversed(no)):
        value += pow(sbase, p) * src[c]

    r = []
    while value:
        value, rem = value / dbase, value % dbase
        r.append( dst[rem] )

    print ''.join(reversed(r))

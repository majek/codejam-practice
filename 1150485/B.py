import sys


def solve(t):
    if not Points:
        return True
    x = -1e14
    for p, v in Points:
        x = max(x + D, p - t) + (v - 1) * D
        if x > p + t:
            return False
    return True


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    C, D = map(int, raw_input().split())
    Points = []
    for _ in xrange(C):
        p, v = map(int, raw_input().split())
        Points.append( (p, v) )

    Points.sort()

    if solve(0):
        print '%.6f' % (0,)
        continue

    l = 0.; r = 1.
    while solve(r) == False:
        r *= 2
    while True:
        m = (l+r) / 2.
        if m == l or m == r:
            break
        if not solve(m):
            l = m
        else:
            r = m

    print '%.6f' % (l,)


import sys
import itertools
import math



def count_delay(A, t0, x0):
    # x0 = 0.5 * A * T**2
    # we need to accelerate for at least
    T = math.sqrt(2*(x0 / float(A)))
    if t0 > T:
        td = t0 - T
        return td
    return 0

def where_we(A, tdelay, t):
    # nowhere for tdelay
    t -= tdelay
    if t < 0:
        return 0
    # accelerating for t
    return 0.5 * A * (t**2)



def solve(T, A, D):
    # time till distance D
    tdelay = 0.
    tt = math.sqrt(2*(D / float(A)))

    for (t0, x0), (t1, x1) in itertools.izip(T, T[1:]):
        # car will be at x1 at t1
        # we will be at
        if where_we(A, tdelay, t1) > x1:
            # too fast
            # print "a=%s tdelay=%s car:(%s %sm) we: %sm" % (A, tdelay, t1, x1, where_we(A, tdelay, t1))
            tdelay = count_delay(A, t1, x1)
    return tdelay + tt


def normalize(T, D):
    t0, x0 = T[0]
    if x0 >= D:
        return
    yield (t0, x0)
    for (t0, x0), (t1, x1) in itertools.izip(T, T[1:]):
        tm =  float(t1 - t0) / (x1 - x0)
        def when_car(x):
            assert x0 <= x <= x1
            return t0 + (x - x0) * tm
        if x0 < D <= x1:
            if D == x1:
                yield (t1, D)
            else:
                yield (when_car(D), D)
            break
        else:
            assert x0 <= x1 < D
            yield (t1, x1)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no ,)
    print "Case #%s:" % (case_no,)

    D, N, _ = raw_input().split()
    D = float(D)
    N = int(N)
    T = [map(float, raw_input().split()) for _ in xrange(N)]
    # print 'pre  :', D, T
    T = list(normalize(T, D))
    # print 'post :', D, T
    assert not T or T[-1][1] == D

    for A in map(float, raw_input().split()):
        print '%.6f' % (solve(T, A, D),)

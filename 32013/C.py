from math import *

def circle_ar(r):
    return pi * (r**2.)

def segment_ar(r, d):
    assert d > 0.
    if d > r: return 0.
    theta = 2 * acos( d / r )
    return ((r**2.) / 2.) * (theta - sin(theta))

def quad_area(r, x0, y0, x1, y1):
    if ()

for case_no in xrange(input()):
    f, R, t, r, g = [float(v) for v in raw_input().split()]

    ring_area = circle_ar(R) - circle_ar(R-t)
    print 2* segment_ar(R-t, R-t-0.1)


    print "Case #%s: %.6f" % (case_no + 1, 0.1)

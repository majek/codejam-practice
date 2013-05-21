import sys
import math

sys.setrecursionlimit(100000)


def swarm(t):
    X = (Xs + Xv * t) / float(N)
    Y = (Ys + Yv * t) / float(N)
    Z = (Zs + Zv * t) / float(N)
    return math.sqrt(X**2 + Y**2 + Z**2)

def ternarysearch(l, r):
    assert r > l
    if r - l < 0.000000001:
        return (l+r) / 2.
    lt = (2*l + r) / 3.
    rt = (l + 2*r) / 3.
    if swarm(lt) > swarm(rt):
        return ternarysearch(lt, r)
    else:
        return ternarysearch(l, rt)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    Xs = Ys = Zs = Xv = Yv = Zv = 0.

    N = input()
    for _ in xrange(N):
        x, y, z, vx, vy, vz = map(int, raw_input().split())
        Xs += x
        Ys += y
        Zs += z
        Xv += vx
        Yv += vy
        Zv += vz

    if swarm(-1) <= swarm(0):
        ans = 0
    else:
        b = 2
        while swarm(0) > swarm(b):
            b = b ** 2
        ans = ternarysearch(0., b)

    print '%.6f %.6f' % (swarm(ans), ans)

import collections
import itertools
import sys
import math
import random


distance = lambda a,b,c,d: math.sqrt((a-c)**2 + (b-d)**2)

def collide(x, y, r):
    for cx, cy, cr, _ in D:
        if distance(x, y, cx, cy) < cr + r:
            return True
    return False


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, W, L = map(int, raw_input().split())
    R = list(enumerate(map(int, raw_input().split())))

    R.sort(reverse=True, key=lambda (i, r): r)
    D = []

    # Try put biggest in corners
    corners = [(0, 0), (W, 0), (W, L), (0, L)]
    for x, y in corners:
        for i, r in R[:]:
            if not collide(x, y, r):
                D.append( (x, y, r, i) )
                R.remove( (i, r) )

    # Try to put rest on edges?

    for i, r in R:
        while True:
            x = random.uniform(0, W)
            y = random.uniform(0, L)
            if not collide(x, y, r):
                D.append( (x, y, r, i) )
                break
    D.sort(key=lambda (x,y,r,i):i)
    print ' '.join(['%f %f' % (x, y) for x, y, _, _ in D])

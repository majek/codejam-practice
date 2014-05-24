import itertools
import sys
import collections


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())
    Sx, Sy, Ex, Ey = map(lambda s:int(s), raw_input().split())

    A = [map(int, raw_input().split()) for _ in xrange(N)]

    def neighbours(x, y):
        if x > 0:
            yield x-1, y
        if x < N-1:
            yield x+1, y
        if y > 0:
            yield x, y-1
        if y < M-1:
            yield x, y+1

    C = [[(Ellipsis, None)] * M for x in xrange(N)]

    level = collections.defaultdict(set)
    level[0].add( (Sx, Sy) )
    C[Sx][Sy] = (0, -A[Sx][Sy])

    while level:
        mcost = min(level.iterkeys())
        mcostitems = level[mcost]
        del level[mcost]

        for x, y in mcostitems:
            xycost = C[x][y]
            for a, b in neighbours(x, y):
                if A[a][b] < 0:
                    continue
                abcost = xycost[0]+1, xycost[1]-A[a][b]
                if abcost < C[a][b]:
                    C[a][b] = abcost
                    level[xycost[0]+1].add( (a,b) )

    if C[Ex][Ey][0] is Ellipsis:
        print "Mission Impossible."
    else:
        print -C[Ex][Ey][1]


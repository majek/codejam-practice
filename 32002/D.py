import itertools
import sys
import collections

import array


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    R, C, Rsz = map(int, raw_input().split())
    restricted = [map(lambda i:int(i)-1, raw_input().split()) for _ in xrange(Rsz)]

    emptyrow = [0] * C
    A = [array.array('H', emptyrow) for _ in xrange(R)]
    B = [array.array('B', emptyrow) for _ in xrange(R)]
    for a, b in restricted:
        B[a][b] = 1

    def neigh(r, c):
        if r + 2 < R and c + 1 < C:
            yield r+2, c+1
        if r + 1 < R and c + 2 < C:
            yield r+1, c+2

    A[0][0] = 1
    level = [(0,0)]
    while level:
        newlevel = set()
        for r, c  in level:
            for a, b in neigh(r,c):
                if B[a][b] != 0:
                    continue
                A[a][b] = (A[a][b] + A[r][c]) % 10007
                newlevel.add( (a,b) )
        level = newlevel

    print A[R-1][C-1]



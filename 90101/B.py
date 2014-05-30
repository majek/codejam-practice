from collections import defaultdict
import string
import sys



for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,)

    H, W = map(int, raw_input().split())
    A = [map(int, raw_input().split()) for _ in xrange(H)]
    B = [[None] * W for _ in xrange(H)]

    if H == 1 and W == 1:
        print "a"
        continue

    def neigh(r,c):
        if r > 0:
            yield r-1, c
        if c > 0:
            yield r, c-1
        if c < W-1:
            yield r, c+1
        if r < H-1:
            yield r+1, c

    basins = list(reversed(string.ascii_uppercase))

    sinks = []
    for r, c in ((r, c) for r in xrange(H) for c in xrange(W)):
        a, b = min(neigh(r,c), key=lambda (a,b):A[a][b])
        if A[r][c] <= A[a][b]:
            B[r][c] = basins.pop()
            sinks.append( (r,c) )

    for r, c in sinks:
        v = B[r][c]
        level = [ (r,c) ]
        while level:
            nlevel = []
            for a, b in level:
                B[a][b] = v
                for c, d in neigh(a,b):
                    if B[c][d]: continue
                    x,y = min(neigh(c,d ), key=lambda (a,b):A[a][b])
                    if B[x][y] != v: continue
                    nlevel.append( (c,d) )
            level = set(nlevel)

    b = list(reversed(string.ascii_lowercase))

    m = {}
    for r in B:
        for c in r:
            if c not in m:
                m[c] = b.pop()
            print m[c],
        print

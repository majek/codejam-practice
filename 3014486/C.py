import sys
import string
import itertools
import collections

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    W, H, B = map(int, raw_input().split())
    G = [[1] * W for _ in xrange(H)]


    for _ in xrange(B):
        x0, y0, x1, y1 = map(int, raw_input().split())
        for x in xrange(x0, x1+1):
            for y in xrange(y0, y1+1):
                G[y][x] = 0

    Gb = []
    prow = None
    for row in G:
        if row != prow:
            Gb.append(row)
            prow = row
    #G = Gb

    F = collections.defaultdict(lambda:collections.defaultdict(lambda:0))
    for r in xrange(len(G)):
        for c in xrange(W):
            if G[r][c] != 1:
                continue
            F[(r, c)][(r,c, 'o')] += 1
            F[(r, c, 'i')][(r,c)] += 1
            if r == 0:
                F[None][(r,c,'i')]+=1
            if r == len(G) - 1:
                F[(r, c, 'o')][ Ellipsis ] += 1
            if c < W-1 and G[r][c+1] == 1:
                F[(r, c, 'o')][(r, c+1,'i')] += 1
            if c > 0 and G[r][c-1] == 1:
                F[(r, c,'o')][(r, c-1,'i')] += 1
            if r < len(G)-1 and G[r+1][c] == 1:
                F[(r, c,'o')][(r+1, c,'i')] += 1
            if r > 0 and G[r-1][c] == 1:
                F[(r, c,'o')][(r-1, c,'i')] += 1

    def flow():
        level = [None]
        prev = {None: None}
        while level and Ellipsis not in prev:
            new_level = []
            for n in level:
                for c, v in F[n].iteritems():
                    if c in prev or v < 1:
                        continue
                    prev[c] = n
                    new_level.append( c )
            level = new_level

        if Ellipsis not in prev:
            return False

        e = Ellipsis
        while e is not None:
            p = prev[e]
            F[p][e] -= 1
            if not F[p][e]:
                del F[p][e]
                if not F[p]:
                    del F[p]
            F[e][p] += 1
            e = p
        return True

    c = 0
    while flow():
        c += 1
    print c

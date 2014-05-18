import itertools
import sys
import math



def dim_ternarysearch_min(l, r, fun, depth=1024):
    if depth == 0:
        return r
    dim = len(l)
    lt = [(2.*l[i] + r[i]) / 3. for i in xrange(dim)]
    rt = [(l[i] + 2.*r[i]) / 3. for i in xrange(dim)]

    if r == rt  or l == lt:
        return l

    lts = [None] * dim
    rts = [None] * dim
    for d in xrange(dim):
        a = l[:]
        a[d] = lt[d]
        lts[d] = fun(*a)

        b = r[:]
        b[d] = rt[d]
        rts[d] = fun(*b)

    mc = min(lts + rts)
    for d in xrange(dim):
        #print >> sys.stderr, d
        if lts[d] != mc and rts[d] != mc:
            continue
        if lts[d] > rts[d]:
            #a = l[:]
            #a[d] = lt[d]
            return dim_ternarysearch_min(a, r, fun, depth-1)
        else:
            #b = r[:]
            #b[d] = rt[d]
            return dim_ternarysearch_min(l, b, fun, depth-1)




dist = lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2 + (y1-y2)**2)


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    P = [map(int, raw_input().split()) for _ in xrange(N)]

    def minr(g):
        if not g:
            return 0
        if len(g) == 1:
            return P[list(g)[0]][2]

        rr = []
        for i, j in itertools.combinations(g, 2):
            x1, y1, r1 = P[i]
            x2, y2, r2 = P[j]
            rr.append( dist(x1, y1, x2, y2) + r1 + r2)

        return max(rr)/2

    m = Ellipsis
    allg = set(range(N))
    for g in itertools.chain(*(itertools.combinations(range(N), m)
                               for m in xrange(N))):
        g1 = set(g)
        g2 = allg - g1
        m = min(m, max(minr(g1), minr(g2)))
    print '%.6f' % m


import sys


def solve((b, c)):
    # print b,c, W[b], W[c], D[b], D[c]
    p = []
    for a in W[b] & rev_d[D[b]-1]:
        gkey = (a, b, c); fkey = (a, b)
        if fkey not in F:
            solve(fkey)
        p.append( F[fkey] + G[gkey] )
    F[(b, c)] = max(p)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    P, _ = map(int, raw_input().split())

    W = [set() for _ in xrange(P)]
    for pair in raw_input().split():
        a, b = map(int, pair.split(","))
        W[a].add( b )
        W[b].add( a )

    # 1. Distances
    D = [Ellipsis] * P
    done = set()
    level = set((0,))
    d = 0
    while level and 1 not in done:
        nlevel = set()
        for p in level:
            D[p] = d
            nlevel |= W[p]
        done |= level
        level = nlevel - done
        d += 1

    # 2. Index of distances
    rev_d = [set() for _ in xrange(d)]
    for p, d in enumerate(D):
        if d is not Ellipsis:
            rev_d[d].add( p )

    G = {}
    for d in xrange(len(rev_d)-2):
        for a in rev_d[d]:
            for b in W[a] & rev_d[d+1]:
                for c in W[b] & rev_d[d+2]:
                    G[(a, b, c)] = len(W[c] - W[a] - W[b])

    F = {}
    for p in rev_d[1]:
        F[(0, p)] = len(W[p] | W[0])

    if 1 in W[0]:
        print 0, len(W[0])
    else:
        prev = []
        for a in rev_d[D[1]-2]:
            for b in W[a] & rev_d[D[1]-1]:
                if 1 not in W[b]:
                    continue
                if (a, b) not in F:
                    solve((a, b))
                prev.append( F[(a, b)] )
        print D[1] - 1, max(prev) - D[1]

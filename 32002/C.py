import sys
import collections
import itertools


def bipartite(G):
    A = set(G.keys())
    B = set(itertools.chain(*G.values()))
    assert not set(A) & set(B)
    assert None not in G and Ellipsis not in G

    G[None] = A
    for k in B:
        G[k].add(Ellipsis)

    def find_path(G):
        level = [None]
        prev = {}
        while level and Ellipsis not in prev:
            newlevel = []
            for node in level:
                for child in G[node]:
                    if child in prev:
                        continue
                    prev[child] = node
                    newlevel.append( child )
            level = newlevel

        if Ellipsis not in prev:
            return False

        e = Ellipsis
        while e is not None:
            p = prev[e]
            G[p].remove(e)
            if not G[p]:
                del G[p]
            G[e].add(p)
            e = p
        return True

    while find_path(G):
        pass
    return [(list(G[b])[0], b) for b in G[Ellipsis]]


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    M, N = map(int, raw_input().split())
    broken = [list(raw_input()) for _ in xrange(M)]

    def neigh(r, c):
        if c > 0: yield r, c - 1
        if c < N-1: yield r, c + 1
        if r > 0:
            if c > 0: yield r - 1, c - 1
            if c < N-1: yield r - 1, c + 1
        if r < M-1:
            if c > 0: yield r + 1, c - 1
            if c < N-1: yield r + 1, c + 1

    G = collections.defaultdict(set)
    for r, c in ((r, c) for r in xrange(M) for c in xrange(N)):
        for a, b in neigh(r, c):
            if broken[r][c] == 'x' or broken[a][b] == 'x':
                continue
            if c % 2 == 1:
                G[(r,c)].add( (a,b) )

    print M*N - sum(sum(c == 'x' for c in r) for r in broken) - len(bipartite(G))

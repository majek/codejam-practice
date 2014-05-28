import collections
import itertools
import sys


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

    N, K = map(int, raw_input().split())
    P = [map(int, raw_input().split()) for _ in xrange(N)]

    above = [set(range(N)) for _ in xrange(N)]
    for row in zip(*P):
        for n in xrange(N):
            v = row[n]
            above[n] &= set(i for i in xrange(N) if row[i] > v)

    G = collections.defaultdict(set)
    for n, s in enumerate(above):
        G[n] = set(i+N for i in s)

    to = set(b-N for a, b in bipartite(G))
    print len(set(range(N)) - to)

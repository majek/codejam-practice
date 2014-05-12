import sys
from collections import defaultdict
from itertools import combinations
from array import array

for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),
    print >> sys.stderr, "Case #%s:" % (case_no,)

    N = input()

    E = defaultdict(set)
    for _ in xrange(N-1):
        x, y = map(int, raw_input().split())
        E[x-1].add( y-1 )
        E[y-1].add( x-1 )

    M = N + 1
    mem1 = array('h', (-1 for _ in xrange(M**2)))

    def children(parent, child):
        r = mem1[parent * M + child]
        if r is -1:
            child_edges = E[child] - set((parent,))
            r = len(child_edges) + sum(children(child, n) for n in child_edges)
            mem1[parent * M + child] = r
        return r

    def solve(parent, child):
        child_edges = E[child] - set((parent,))

        vmin = all_children = children(parent, child)
        for a, b in list(combinations(child_edges, 2)):
            vmin = min(vmin,
                       all_children - children(child, a) - children(child, b) - 2 +
                       solve(child, a) +
                       solve(child, b))
        return vmin


    print min(solve(N, i) for i in xrange(N))

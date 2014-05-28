import sys
import collections


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

    G = collections.defaultdict(lambda:collections.defaultdict(lambda:0))
    for r in xrange(M):
        for c in xrange(N):
            for a, b in neigh(r, c):
                if broken[r][c] == 'x' or broken[a][b] == 'x':
                    continue
                if c % 2 == 1:
                    G[(None,None)][(r,c)] = 1
                    G[(r,c)][(a,b)] = 1
                else:
                    G[(r,c)][(Ellipsis,Ellipsis)] = 1

    def find_path(G, s, e):
        level = [(s)]
        prev = {s:None}
        while level and e not in prev:
            newlevel = set()
            for node in level:
                for child, v in G[node].iteritems():
                    if child in prev: continue
                    assert v > 0
                    prev[child] = node
                    newlevel.add( child )
            level = newlevel
        if e not in prev:
            return None

        while prev[e]:
            p = prev[e]
            assert G[p][e] > 0
            v = G[p][e]
            if v != 1:
                G[p][e] -= 1
            else:
                del G[p][e]
            G[e][p] += 1
            e = p
        return True

    s, e = (None, None), (Ellipsis, Ellipsis)
    while find_path(G, s, e):
        pass

    print M*N - sum(sum(1 for c in r if c == 'x') for r in broken) - len(G[(Ellipsis, Ellipsis)])

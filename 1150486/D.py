import sys
import collections
import itertools


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    P, _ = map(int, raw_input().split())
    G = collections.defaultdict(set)
    for pair in raw_input().split():
        x, y = map(int, pair.split(","))
        G[x].add(y)
        G[y].add(x)

    level = set([0])
    prev = collections.defaultdict(list)
    done = set()
    while 1 not in level:
        new_level = []
        for p in level:
            for t in G[p] - done:
                prev[t].append(p)
                new_level.append(t)
        done |= set(new_level)
        level = set(new_level)

    e = 1
    depth = 0
    while e != 0:
        depth += 1
        e = prev[e][0]

    def solve(p, threats):
        threats = G[p] | threats
        if p == 0:
            return len(threats)
        return max(solve(t, threats) for t in prev[p])


    r = max(solve(p, set((0,))) for p in prev[1])
    print depth-1, r - 1-(depth-1)

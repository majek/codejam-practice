import collections
import itertools
import sys
import math
import string

DIGITS = set(string.digits)

def do_move(fields, (a, b)):
    for r, c in fields:
        rp = r + a
        cp = c + b
        if M[rp][cp] != '#':
            yield (rp, cp)
        else:
            yield (r, c)

def solve(compr, reach):
    if len(compr) == 1:
        return True

    for move in [(0, -1), (0, 1), (1, 0)]:
        ncompr = set(do_move(compr, move))
        k = frozenset(ncompr)
        if k in mem: continue
        mem[k] = True
        #print compr, move, ncompr
        if len(ncompr) <= len(compr) and len(ncompr - reach) == 0:
            # Reduced number of unique points and not moved anyone
            # beyond our range.
            if solve(ncompr, reach):
                return True
    return False


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,)

    R, C = map(int, raw_input().split())
    M = [list(raw_input()) for _ in xrange(R)]

    caves = {}
    for r, row in enumerate(M):
        for c, v in enumerate(row):
            if v in DIGITS:
                caves[int(v)] = (r, c)

    reachable = [None] * (max(caves.iterkeys())+1)
    for cave, cave_pos in caves.iteritems():
        reachable[cave] = reach = set()
        layer = set([cave_pos])
        while layer:
            nlayer = set()
            for r, c in layer:
                for a, b in [(r, c-1), (r, c+1), (r-1, c)]:
                    if M[a][b] != '#':
                        nlayer.add( (a, b) )
            nlayer -= reach
            reach |= layer
            layer = nlayer
    # for cave, reach in enumerate(reachable):
    #     print cave, reach


    for cave, reach in enumerate(reachable):
        mem = {}
        r = solve(reach.copy(), reach)
        print '%s: %s %s' % (cave, len(reach), 'Lucky' if r else 'Unlucky')


import collections
import itertools
import sys
import math


def get_cycles(n, path, xx):
    path = path + [n]
    for c in Vertex[n]:
        if c not in path:
            get_cycles(c, path, Cycles)
        else:
            if c != path[-2]:
                i = path.index(c)
                xx.add( frozenset(path[i:]) )


def okay(colors, r, good):
    for g in good:
        s = set([r[n] for n in g])
        if len(s) != colors:
            return False
    return True


def try_colors(colors, good):
    r = [0] * N
    def blah(i):
        for c in range(colors):
            r[i] = c
            if i == 0:
                x = nah()
                if x: return x
            else:
                x = blah(i-1)
                if x: return x
    def nah():
        if okay(colors, r, good):
            return r
        return None
    return blah(N-1)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())
    U = map(lambda w:int(w)-1, raw_input().split())
    V = map(lambda w:int(w)-1, raw_input().split())

    Vertex = collections.defaultdict(list)
    for a, b in itertools.chain(zip(range(N), range(1, N) + [0]), zip(U, V)):
        Vertex[a].append( b )
        Vertex[b].append( a )

    for v in Vertex.itervalues():
        v.sort()

    # worst way of getting rooms
    Cycles = set()
    get_cycles(0, [], Cycles)
    good = []
    for c in sorted(Cycles, key=lambda a:len(a)):
        for g in good:
            if c & g == g:
                 break
        else:
            good.append( c )

    for colors in range(min(map(len, good)), 0, -1):
        r = try_colors(colors, good)
        if r is not None:
            print colors
            print ' '.join([str(c+1,) for c in r])
            break


import sys
import collections
import itertools

def concat(z, i):
    if i is Ellipsis:
        return Ellipsis
    return int(str(z) + str(i))


for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),
    print >>sys.stderr, "Case #%s:" % (case_no,)

    N, M = map(int, raw_input().split())
    zips = [input() for i in xrange(N)]
    stowns = sorted(xrange(N), key=lambda t:zips[t])

    flights = collections.defaultdict(set)
    for a, b in [map(int, raw_input().split()) for _ in xrange(M)]:
        flights[a-1].add( b-1 )
        flights[b-1].add( a-1 )

    def xcanreach(canflyto, todo):
        while todo and canflyto:
            canflyto = reduce(lambda acc, n: acc|flights[n], canflyto, set()) & todo
            todo -= canflyto
        return bool(canflyto)

    def solve(stack, todo):
        if not todo:
            return ''

        canvisit = []
        for n in xrange(len(stack)):
            for f in flights[stack[n]] & todo:
                canvisit.append( (f, n) )
        canvisit.sort(key=lambda (f, i):(zips[f], N-i))

        for f, n in canvisit:
            xstack = stack[:n+1] +[f]
            xtodo = todo - set((f,))
            if not xcanreach(set(xstack), xtodo):
                continue
            return str(zips[f]) + solve(stack[:n+1] + [f], todo - set((f,)))

    t = min(xrange(N), key=lambda t:zips[t])
    print str(zips[t]) + solve([t], set(xrange(N))-set((t,)))

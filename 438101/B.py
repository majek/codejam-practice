import sys


def solve():
    cars = []
    for t, ps in enumerate(Towns):
        if t == T-1:
            cars.append( 0 )
            continue
        ps.sort()
        c = 0
        while ps:
            p = ps.pop()
            c += 1
            if not p:
                return -1
            ps = ps[p-1:]
        cars.append( c )
    return cars

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, T = map(int, raw_input().split())
    E = input()

    Towns = [list() for _ in xrange(N)]
    for _ in xrange(E):
        H, P = map(int, raw_input().split())
        Towns[H-1].append( P )

    cars = solve()
    print ' '.join(str(c) for c in cars) \
        if cars != -1 else "IMPOSSIBLE"


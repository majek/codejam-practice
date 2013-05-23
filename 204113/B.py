import sys


def fall((r, c)):
    f = 0
    while (r+1, c) in Air:
        f += 1
        r += 1
    return f

def accessible((r, c), air):
    yield (r, c)
    assert (r+1, c) not in air
    for chain in [xrange(c-1, 0-1, -1), xrange(c+1, C)]:
        for cc in chain:
            if (r, cc) in air:
                f = fall((r, cc))
                if f == 0:
                    yield (r, cc)
                    continue
                if f <= F:
                    for xx, yy in accessible((r+f, cc), air):
                        yield (xx, yy)
            break

def can_dig((r, c), air):
   if (r, c-1) in air and ((r+1, c-1) not in air):
       yield (r+1, c-1)
   if (r, c+1) in air and ((r+1, c+1) not in air):
       yield (r+1, c+1)


def solve((r, c), dug):
    dug = frozenset(dug)
    k = (r, c, dug)
    if k in mem: return mem[k]

    ans = mem[k] = _solve((r, c), dug)
    return ans

def _solve(pos, dug):
    air = Air | dug
    acc = list(accessible(pos, air))

    diggable = set()
    for p2 in acc:
        if p2[0] == R-1:
            return 0
        for p3 in can_dig(p2, air):
            diggable.add(p3)


    ans = sys.maxint
    for rr, cc in acc:
        dug2 = set()
        f = fall((rr+1, cc+1))
        if f+1 <= F:
            for cci in xrange(cc+1, C):
                if (rr+1, cci) not in diggable:
                    break
                dug2.add( (rr+1, cci) )
                ans = min(ans, len(dug2) + solve((rr+1+f, cc+1), dug2 if f == 0 else set()))
        dug2 = set()
        f = fall((rr+1, cc-1))
        if f+1 <= F:
            for cci in xrange(cc-1, 0-1, -1):
                if (rr+1, cci) not in diggable:
                    break
                dug2.add( (rr+1, cci) )
                ans = min(ans, len(dug2) + solve((rr+1+f, cc-1), dug2 if f == 0 else set()))
    return ans


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    R, C, F = map(int, raw_input().split())
    M = [raw_input() for _ in xrange(R)]
    Air = set((r, c) for c in xrange(C) for r in xrange(R) if M[r][c] == '.')

    mem = {}
    a = solve((0,0), set())
    if a >= sys.maxint:
        print "No"
    else:
        print "Yes %s" % (a,)

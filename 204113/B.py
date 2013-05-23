import sys


def fall((r, c), air):
    f = 0
    while (r+1, c) in air:
        f += 1
        r += 1
    return f

def accessible((r, c), air):
    yield (r, c)
    assert (r+1, c) not in air
    for chain in [xrange(c-1, 0-1, -1), xrange(c+1, C)]:
        for cc in chain:
            if (r, cc) in air:
                f = fall((r, cc), air)
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
    dug = frozenset((rr, cc) for rr, cc in dug if rr in (r, r+1))
    k = (r, c, dug)
    if k in mem: return mem[k]

    ans = mem[k] = _solve((r, c), dug)
    return ans

def _solve(pos, dug):
    air = Air | dug
    acc = list(accessible(pos, air))
    for (rr, cc) in acc:
        if rr == R-1:
            return 0
    answers = [sys.maxint]
    for p2 in acc:
        for p3 in can_dig(p2, air):
            a = 1 + solve(p2, dug | set((p3,)))
            answers.append( a )
    return min(answers)


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

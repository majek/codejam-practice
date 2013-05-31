import sys
import itertools


def is_valid(F):
    for i, t, j, k in S:
        if t in 'TL':
            x = (t, F[j])
            if x in (('T', True), ('L', False)):
                if F[i] != True:
                    return False
            else:
                if F[i] != False:
                    return False
        else:
            x = (t, (F[j] == F[k]))
            if x in (('S', True), ('D', False)):
                if F[i] != True:
                    return False
            else:
                if F[i] != False:
                    return False
    return True

def solve():
    valid = []

    # Go through all 2**N options yeah!
    for F in itertools.product(*[(False, True)] * N):
        if is_valid(F):
            valid.append( F )

    dd = {frozenset([True]): 'T',
          frozenset([False]): 'L',
          frozenset([True, False]): '-'}
    for i, k in enumerate(zip(*valid)):
        yield dd[frozenset(k)]


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())

    I = [list() for _ in xrange(N)]
    S = []
    for _ in xrange(M):
        e = raw_input().split()
        S.append( (int(e[0]) - 1,
                   e[1],
                   int(e[2]) - 1,
                   int(e[3]) - 1 if len(e) == 4 else None) )

    print ' '.join(solve())

import sys
from collections import Counter


for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),
    print >> sys.stderr, "Case #%s:" % (case_no,)

    N, L = map(int, raw_input().split())
    O = raw_input().split()
    D = raw_input().split()
    D.sort()

    flip = [False] * L

    I = {
        True:{'1':'0','0':'1'},
        False:{'0':'0', '1':'1'},
        }

    def solve(l):
        oo = [''.join(I[f][c] for f, c in zip(flip, o))
                   for o in O]
        oo = [o[:l] for o in oo]
        oo.sort()
        dd = [d[:l] for d in D]
        if dd != oo:
            return False

        if l == L:
            return True

        flip[l] = False
        if solve(l+1):
            return True
        flip[l] = True
        return solve(l+1)

    if not solve(0):
        print "NOT POSSIBLE"
    else:
        print sum(flip)

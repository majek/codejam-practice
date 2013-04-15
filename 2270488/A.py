import sys
import itertools
import collections

for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,), 

    B = [list(raw_input()) for _ in range(4)]
    raw_input()

    lines = []
    lines.extend( B )
    cols = [[B[i][j] for i in range(4)] for j in range(4)]
    lines.extend( cols )
    d1 = [B[i][i] for i in range(4)]
    d2 = [B[3-i][i] for i in range(4)]
    lines.extend( [d1, d2] )

    done = False
    for ll in [set(l) for l in lines]:
        if ll - set('T') == set(['X']):
            print 'X won'
            done = True
            break
        elif ll - set('T') == set(['O']):
            print 'O won'
            done = True
            break
    if not done:
        allc = set(B[0]) | set(B[1]) | set(B[2]) | set(B[3])
        if '.' in allc:
            print 'Game has not completed'
        else:
            print 'Draw'

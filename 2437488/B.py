import sys
import itertools


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    X, Y = map(int, raw_input().split())
    XY = abs(X) + abs(Y)

    seq_sum = 0
    for seq_item in itertools.count(1):
        seq_sum += seq_item
        if seq_sum >= XY:
            break

    while True:
        x = X; y = Y; path = []
        for n in xrange(seq_item, 0, -1):
            if abs(x) > abs(y):
                if x > 0:
                    x -= n
                    path.append( 'E' )
                else:
                    x += n
                    path.append( 'W' )
            else:
                if y > 0:
                    y -= n
                    path.append( 'N' )
                else:
                    y += n
                    path.append( 'S' )
        if x == 0 and y == 0:
            break
        seq_item += 1

    print ''.join(reversed(path))


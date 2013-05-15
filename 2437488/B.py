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
    path.reverse()

    xx = 0; yy = 0; s = 1
    for c in path:
        if c == 'E':
            xx += s
        elif c == 'W':
            xx -= s
        elif c == 'N':
            yy += s
        elif c == 'S':
            yy -= s
        else:
            assert 0
        s += 1
    assert X == xx, (X, xx, path)
    assert Y == yy, (Y, yy, path)
    print ''.join(path)


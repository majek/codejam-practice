import sys
import collections


left = {(0,  1): (1,  0), (1,  0): (0, -1),
        (0, -1): (-1, 0), (-1, 0): (0,  1)}

mask = {(0,  1): 0x2, (1,  0): 0x8,
        (-1, 0): 0x4, (0, -1): 0x1}

move = lambda (a, b), (c, d): (a+c, b+d)
inv = lambda (a, b): (-a, -b)

for case_no in xrange(1, input()+1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,)

    forward_backward = raw_input()
    start = (0, 1); end = None
    d = (0, 1); p = start

    board = collections.defaultdict(lambda: 0)
    for c in forward_backward:
        if c == 'W':
            board[p] |= mask[d]
            p = move(p, d)
            board[p] |= mask[inv(d)]
        elif c == ' ':
            end = p
            d = inv(d)
        else:
            d = left[d if c == 'L' else inv(d)]
    del board[start]
    del board[end]
    keys = board.keys()
    min_x = min(a for a,b in keys)
    max_x = max(a for a,b in keys)
    min_y = min(b for a,b in keys)
    max_y = max(b for a,b in keys)

    for y in range(min_y, max_y+1):
        print ''.join('%x' % board[(x, y)] for x in range(min_x, max_x+1))



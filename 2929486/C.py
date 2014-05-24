import itertools
import sys
import collections


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()

    A = [list(raw_input()) for _ in xrange(N)]

    B = sum(c == 'B' for r in A for c in r)
    R = sum(c == 'R' for r in A for c in r)
    if abs(B-R) > 1:
        print "Impossible"
        continue

    def neig(x, y):
        if y < N-1:
            yield x, y+1
        if x > 0:
            if y < N-1:
                yield x-1, y+1
            yield x-1, y
        if x < N-1:
            yield x+1, y
        if y > 0:
            if x < N-1:
                yield x+1, y-1
            yield x, y-1

    def path(x, y, color, mem={}):
        mem[(x,y)] = True

        assert A[x][y] == color
        if (color == 'B' and y == N-1) or (color == 'R' and x == N-1):
            return [(x,y)]
        for a, b in neig(x, y):
            if A[a][b] != color or (a,b) in mem:
                continue
            c = path(a, b, color, mem)
            if c:
                return [(x, y)] + c
        #del mem[(x,y)]
        return []

    def findpath(color):
        if color == 'R':
            for y in (y for y in xrange(N) if A[0][y] == 'R'):
                p = path(0, y, 'R', {})
                if p:
                    return p
        else:
            for x in (x for x in xrange(N) if A[x][0] == 'B'):
                p = path(x, 0, 'B', {})
                if p:
                    return p

    red = blue = 0
    pb = findpath('B')
    pr = findpath('R')
    if pb:
        blue = 2
        for a, b in pb:
            A[a][b] = '?'
            if not findpath('B'):
                blue = 1
                break
            A[a][b] = 'B'
    if pr:
        red = 2
        for a, b in pr:
            A[a][b] = '?'
            if not findpath('R'):
                red = 1
                break
            A[a][b] = 'R'

    if blue and red:
        assert 0
    elif blue > 1 or red > 1:
        print "Impossible"
    elif blue == 0 and red == 0:
        print "Nobody wins"
    elif blue and B >= R:
        print "Blue wins"
    elif red and R >= B:
        print "Red wins"
    else:
        print "Impossible"

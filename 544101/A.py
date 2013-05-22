import sys

def winning(r, c):
    if r + K <= N:
        if len(set(B[r+k][c] for k in xrange(K))) == 1:
            return True
    if c + K <= N:
        if len(set(B[r][c+k] for k in xrange(K))) == 1:
            return True
    if c + K <= N and r + K <= N:
        if len(set(B[r+k][c+k] for k in xrange(K))) == 1:
            return True
    if c >= K-1 and r + K <= N:
        if len(set(B[r+k][c-k] for k in xrange(K))) == 1:
            return True
    return False


def did_win():
    wc = set()
    for r in xrange(N):
        for c in xrange(N):
            colour = B[r][c]
            if colour != '.':
                if winning(r, c):
                    wc.add( colour )
    return wc

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, K = map(int, raw_input().split())
    B = [list(raw_input()) for _ in xrange(N)]

    for row in B:
        c = N-1
        for i in xrange(N-1, 0-1, -1):
            if row[i] != '.':
                if i != c:
                    row[i], row[c] = row[c], row[i]
                c -= 1
    wc = did_win()
    if wc == set('BR'):
        print 'Both'
    elif 'B' in wc:
        print 'Blue'
    elif 'R' in wc:
        print 'Red'
    else:
        print 'Neither'

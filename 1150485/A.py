import sys

avg = lambda l: sum(l) / float(len(l))

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,)

    N = input()
    Teams = [raw_input() for _ in xrange(N)]

    X = [[None, None, None] for _ in xrange(N)]

    for i in xrange(N):
        wp = (sum(1. for c in Teams[i] if c in '1') /
              sum(1. for c in Teams[i] if c in '01'))
        owp = []
        for j in xrange(N):
            if Teams[i][j] == '.':
                continue
            xp = (sum(1. for k, c in enumerate(Teams[j]) if c == '1' and k != i) /
                  sum(1. for k, c in enumerate(Teams[j]) if c in '01' and k != i))
            owp.append( xp )
        X[i][0] = wp
        X[i][1] = avg(owp)

    for i in xrange(N):
        X[i][2] = avg([X[j][1] for j in xrange(N) if j != i and Teams[i][j] != '.'])

    rpi = [0.25 * wp + 0.50 * owp + 0.25 * oowp for wp, owp, oowp in X]
    for r in rpi:
        print '%.6f' % (r,)


import itertools
import sys

Y = 'zero one two three four five six seven eight nine'.split()
X = '_ _ double triple quadruple quintuple sextuple septuple octuple nonuple decuple'.split()

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    R = []
    no, fmt = raw_input().split()
    l = 0
    for sz in map(int, fmt.split('-')):
        d, l = no[l:l+sz], l+sz
        for _, g in itertools.groupby(d):
            g = list(g)
            v = int(g[0])
            s = len(g)
            if s == 1 or s > 10:
                for _ in xrange(s):
                    R.append(Y[v])
            else:
                R.append( X[s] )
                R.append(Y[v])
    print ' '.join(R)


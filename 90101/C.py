import collections
import sys

WTCJ = "welcome to code jam"

IDX = collections.defaultdict(set)
for i, c in enumerate(WTCJ):
    IDX[c].add(i)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),
    L = list(raw_input())

    M = collections.defaultdict(dict)

    e = [0] * len(WTCJ)

    for c in L:
        for i in IDX[c]:
            if i == 0:
                e[i] += 1
            else:
                e[i] += e[i-1]

    print '%04i' % (e[-1] % 10000,)



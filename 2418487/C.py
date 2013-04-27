import collections
import itertools
import sys
import math
import nzmath.factor.methods as methods
import random



def gen(N, M):
    if (N,M) in mem: return mem[(N,M)]
    all_products = collections.defaultdict(collections.Counter)
    all_sets = sorted(sorted(p) for p in itertools.product(range(2,M+1), repeat=N))

    for setno, sss in enumerate(all_sets):
        for _ in range(1000):
            numbers = [i for i in sss if random.randint(0,1) == 1]
            prod = reduce(lambda a,b:a*b, numbers, 1)
            all_products[prod][setno] += 1

    for prod, ct in all_products.iteritems():
        total = float(sum(ct.itervalues()))
        all_products[prod] = dict((k, v/total) for k, v in ct.iteritems())
    mem[(N,M)] = (all_products, all_sets)
    return mem[(N,M)]


mem = {}

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,)

    R, N, M, K = map(int, raw_input().split())

    all_products, all_sets = gen(N, M)

    for _ in xrange(R):
        P = map(int, raw_input().split())
        r = all_products[P[0]].copy()
        for p in P:
            r1 = all_products[p]
            k1 = set(r.iterkeys()) & set(r1.iterkeys())
            r = dict( (k, r[k] * r1[k]) for k in k1)
        #print [(all_sets[k], v) for k, v in r.iteritems()]
        k, v = max(r.iteritems(), key=lambda (a,b):b)
        print ''.join(map(str, all_sets[k]))

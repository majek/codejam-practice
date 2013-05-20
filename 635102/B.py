import sys


def solve(tree, may_skip):
    if tree is None:
        return 0

    p, left, right = tree
    m = len(may_skip)/2

    can_skip = [n - 1 for n in may_skip]

    return min(p + solve(left, may_skip[:m]) + solve(right, may_skip[m:]),
               solve(left, can_skip[:m]) + solve(right, can_skip[m:]) \
                   if min(can_skip) >= 0 else Ellipsis)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    P = input()
    M = map(int, raw_input().split())

    tree = [None] * 2**P
    for _ in xrange(P):
        prices = map(int, raw_input().split())
        ntree = [(p, tree[j*2], tree[j*2+1]) for j, p in enumerate(prices)]
        tree = ntree
    tree = tree[0]

    print solve(tree, M)

import itertools
import sys


def binominal(n, r):
    p = 1.0
    for i in xrange(r):
        p = p * (n - i) / (i + 1)
    return p

def prob_at_least(heads, tosses, prob):
    return sum(binominal(tosses, h) * (prob ** h) * (prob ** (tosses - h))
               for h in xrange(heads, tosses+1))


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, X, Y = map(int, raw_input().split())
    X = abs(X)

    base = 0
    total = 0
    for i in itertools.count(1, 2):
        new_total = total + i * 2 - 1
        if new_total > N:
            break
        total = new_total
        base = i

    assert total <= N
    assert new_total > N
    assert sum(xrange(base + 1)) == total

    remaining = N - total
    assert remaining >= 0
    slots  = new_total - total
    assert remaining < slots
    side = slots / 2
    assert total + side * 2 + 1 == new_total

    if Y + X <= base - 1:
        r = 1.
    elif Y + X > base + 1:
        r = 0.
    else:
        assert Y + X == base + 1
        if Y == base + 1: # will fall down
            r = 0.
        else:
            # You're given `Y+1` balls and `remaining` tosses what's the
            # probability...
            coins = Y + 1
            tosses = remaining
            if tosses > side:
                fallen = tosses - side
                tosses -= fallen * 2
                coins -= fallen
                if coins <= 0:
                    r = 1.
                else:
                    r = prob_at_least(coins, tosses, 0.5)
            else:
                r = prob_at_least(coins, tosses, 0.5)
    print "%s" % (r,)

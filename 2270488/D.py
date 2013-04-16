import sys
import itertools
from collections import Counter


def possible(keys, closed):
    keys = keys.copy()
    closed = set(closed)
    while closed:
        for chest in closed:
            if len(required_key[chest] - keys) == 0:
                keys += chest_contains[chest]
                closed.remove( chest )
                break
        else:
            return False
    return True

def solve(keys, closed):
    if not closed:
        return []

    if not possible(keys, closed):
        return None

    for chest in sorted(closed):
        if len(required_key[chest] - keys) == 0:
            r = solve(keys + chest_contains[chest] - required_key[chest],
                      closed - set((chest,)))
            if r is not None:
                return [chest] + r
    assert False

for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    _, N = map(int, raw_input().split())
    start_keys = Counter(map(int, raw_input().split()))

    chest_contains = [None] * N
    required_key = [None] * N
    for chest_no in xrange(N):
        l = map(int, raw_input().split())
        chest_contains[ chest_no ] = Counter(l[2:])
        required_key[ chest_no ] = Counter([l[0]])

    end_keys = reduce(lambda a,b: a+b, chest_contains, start_keys)
    end_keys.subtract(reduce(lambda a,b: a+b, required_key, Counter()))
    if sum(1 for k, v in end_keys.items() if v < 0):
        print 'IMPOSSIBLE'
    else:
        path = solve(start_keys, frozenset(range(N)))
        if path is not None:
            print ' '.join(str(chest_no+1) for chest_no in path)
        else:
            print 'IMPOSSIBLE'

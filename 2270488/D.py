import sys
import itertools
from collections import Counter

def sum_counts(a,b):
    a = a.copy()
    for k, v in b.iteritems():
        a[k] += v
        if not a[k]:
            del a[k]
    return a

def sum_chests(chests):
    a = Counter()
    for chest in chests:
        a += chest_to_keys[chest]
    for chest in chests:
        a[opens[chest]] -= 1
    return a


def end_keys_from_opened(opened):
    a = end_keys.copy()
    b = sum_chests(opened)
    for k, v in b.items():
        a[k] -= v
        #assert a[k] >= 0
    return a

mem = None
def solve(start_keys, closed):
    if closed in mem: return None
    if not closed:
        return []

    for chest in sorted(closed):
        if start_keys[opens[chest]] > 0:
            rem_start_keys = start_keys + chest_to_keys[chest] - opens_ct[chest]
            rem_closed = closed - set((chest,))
            if len(rem_closed) > 1:
                #mem_pos.clear()
                if possible(end_keys, rem_closed) is None:
                    continue
            r = solve(rem_start_keys, rem_closed)
            if r is not None:
                return [chest] + r
    mem[closed] = True
    return None


mem_pos = None
def possible(rend_keys, opened):
    if opened in mem_pos: return None
    if not opened: return []

    for chest in sorted(opened,reverse=True):
        if len(chest_to_keys[chest] - rend_keys) == 0:
            r = possible(rend_keys - chest_to_keys[chest] + opens_ct[chest],
                         opened - set((chest,)))
            if r is not None:
                return r + [chest]
    mem_pos[opened] = True
    return None


for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    _, N = map(int, raw_input().split())
    start_keys = Counter(map(int, raw_input().split()))

    chest_to_keys = [None] * N
    opens = [None] * N
    opens_ct = [None] * N
    for chest_no in xrange(N):
        l = map(int, raw_input().split())
        chest_to_keys[ chest_no ] = Counter(l[2:])
        opens[ chest_no ] = l[0]
        opens_ct[ chest_no ] = Counter([l[0]])

    end_keys = sum_counts(start_keys, sum_chests(range(N)))
    if sum(1 for k, v in end_keys.items() if v < 0):
        print 'IMPOSSIBLE'
        continue

    mem = {}
    mem_pos = {}
    path = solve(start_keys, frozenset(range(N)))
    if path is None:
        print 'IMPOSSIBLE'
    else:
        # sanity check
        a = start_keys.copy()
        for chest in path:
            k = opens[chest]
            assert a[k] >= 1
            a[k] -= 1
            a += chest_to_keys[chest]
        print ' '.join(str(chest_no+1) for chest_no in path)

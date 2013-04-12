import sys
import itertools
import collections


for case_no in xrange(0, input()):
    # print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    levels = [tuple(map(int, raw_input().split()))
              for _ in range(input())]
    levels_by_first = collections.OrderedDict(
        (i, set()) for i in sorted(set([a for a, b in levels])))
    levels_by_second = collections.OrderedDict(
        (i, set()) for i in sorted(set([b for a, b in levels])))
    for l, (a, b) in enumerate(levels):
        levels_by_first[a].add( l )
        levels_by_second[b].add( l )

    def do_level(l, lbf, r):
        a = levels[l][r]
        if a not in lbf or l not in lbf[a]:
            return 0
        lbf[a].remove( l )
        if len(lbf[a]) == 0:
            del lbf[a]
        return 1

    levels_done = 0
    points = 0

    while levels_by_second:
        s = levels_by_second.iterkeys().next()
        if points >= s:
            lvs = levels_by_second[s]
            levels_done += len(lvs)
            for l in set(lvs):
                points += do_level(l, levels_by_first, 0)
                points += do_level(l, levels_by_second, 1)
            continue
        lvs = set()
        for s in levels_by_first.iterkeys():
            if points < s: break
            lvs |= levels_by_first[s]
        # lvs has all the fist with affordable price
        if lvs:
            l = max(lvs, key=lambda l:levels[l][1])
            levels_done += 1
            points += do_level(l, levels_by_first, 0)
            continue
        break

    if levels_by_second:
        print "Too Bad"
    else:
        print levels_done

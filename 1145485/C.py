import collections
import itertools
import sys
import math


def solve(hand, deck_idx, tc):
    # I must admit I'm not entirely sure why this one works.
    k = (hand, min(N-deck_idx, tc))
    if k in mem: return mem[k]

    if tc == 0:
        return 0

    # 1. play all the "T" cards
    sc = 0
    while True:
        nhand = hand
        for i in hand:
            c, s, t = Cards[i]
            if t:
                tc += t - 1
                sc += s
                nhand = (nhand - set((i,))) | set(Cards_idx[deck_idx:deck_idx+c])
                deck_idx = deck_idx + c
        if nhand == hand:
            break
        hand = nhand

    assert tc

    # 2. Just play all the C0 cards
    c0_sc = sc
    c0_tc = tc
    c0_hand = filter(lambda i:Cards[i][0] == 0, hand)
    c0_hand.sort(key=lambda i:Cards[i][1], reverse=True)

    for i in c0_hand:
        c, s, t = Cards[i]
        assert t == 0
        assert c == 0
        c0_sc += s
        c0_tc -= 1
        if c0_tc == 0:
            break
    blah = c0_sc

    # 3. Take one C1/C2 card and play it or not.
    for i in hand:
        c, s, t = Cards[i]
        assert t == 0
        if c == 0: continue
        hand = hand - set((i,))
        r = sc + s + solve(hand | set(Cards_idx[deck_idx:deck_idx+c]), deck_idx + c, tc - 1)
        p = sc +     solve(hand, deck_idx, tc)
        blah = max(r, p, blah)
        break
    mem[k] = blah
    return blah

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    Cards = []
    N = input()
    for _ in xrange(N):
        c, s, t = map(int, raw_input().split())
        Cards.append( (c, s, t) )

    for _ in xrange(input()):
        c, s, t = map(int, raw_input().split())
        Cards.append( (c, s, t) )

    Cards_idx = range(len(Cards))
    hand = frozenset(range(N))
    deck_idx = N

    mem = {}
    print solve(hand, deck_idx, 1)

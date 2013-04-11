from collections import defaultdict

for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    P, K, _ = map(int, raw_input().split())
    Freq = map(int, raw_input().split())
    tup = enumerate(Freq)
    dd = defaultdict(list)
    for letter, freq in tup:
        dd[freq].append( letter )
    level = 1
    used = 0
    d = {}
    for freq in reversed(sorted(set(Freq))):
        letters = dd[freq]
        for letter in letters:
            d[letter] = level
            used += 1
            if used >= K:
                level += 1
                used = 0
    print sum(f * d[l]  for l, f in enumerate(Freq))

import collections
from collections import defaultdict
import itertools
import sys
import math
import pprint as pp

pattern = lambda word, alpha: ''.join(('_' if c not in alpha else c) for c in word)

alphabet = None
def solve(words, apos):
    if len(words) <= 1:
        return {0: words[:]}

    all_c = reduce(lambda s, w: s | set(w), words, set())
    while alphabet[apos] not in all_c:
        apos += 1
    groups = defaultdict(list)
    for word in words:
        p = pattern(word, alphabet[:apos+1])
        groups[p].append(word)

    scores = defaultdict(list)
    for p, words in groups.iteritems():
        s = 0 if alphabet[apos] in p else 1
        for a, l in solve(words, apos+1).iteritems():
            scores[a + s].extend( l )
    return scores


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())
    Words = [raw_input() for _ in xrange(N)]
    Alphabets = [raw_input() for _ in xrange(M)]

    all_words = defaultdict(list)
    word_pos = {}
    for i, word in enumerate(Words):
        all_words[len(word)].append( word )
        word_pos[word] = i


    for alphabet in Alphabets:
        scores = defaultdict(list)
        for sz, words in all_words.iteritems():
            for s, w in solve(words, 0).iteritems():
                scores[s].extend(w)
        solutions = scores[max(scores.iterkeys())]
        print min(solutions, key=lambda w:word_pos[w]),
    print



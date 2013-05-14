import collections
import itertools
import sys
import math



def _all_sub(word, s):
    r = []
    if not word:
        return r
    for i in xrange(s+5, len(word)):
        w = word[:i] + '_' + word[i+1:]
        r.append( (w, i) )
    return r

def all_sub(word):
    yield word
    a = _all_sub(word, -5)
    while a:
        x = []
        for w, s in a:
            yield w
            x.extend(_all_sub(w, s))
        a = x


with open("garbled_email_dictionary.txt") as fd:
    Words = [w.strip() for w in fd.readlines()]

all_subw = set()
for word in Words:
    all_subw.update( all_sub(word) )

print >> sys.stderr, "[*] Loaded!"


def all_break(word):
    if not word:
        return True
    for i in xrange(min(len(word)+1, 11), 1-1, -1):
        if word[:i] not in all_subw:
            continue
        if all_break(word[i:]):
            return True
    return False


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    S = raw_input()

    for sw in all_sub(S):
        if all_break(sw):
            print sum(1 for c in sw if c == '_')
            break

    else:
        assert 0

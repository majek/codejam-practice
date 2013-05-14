import sys
import os.path
import cPickle as pickle


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


if not os.path.exists('garbled_email.pickle'):
    with open("garbled_email_dictionary.txt") as fd:
        Words = [w.strip() for w in fd.readlines()]

    all_subw = set()
    for word in Words:
        all_subw.update( all_sub(word) )

    big_tree = {}
    for w in all_subw:
        t = big_tree
        for c in w:
            t = t.setdefault(c, {})
        t['#'] = True
    with open('garbled_email.pickle', 'wb') as fd:
        pickle.dump(big_tree, fd)
else:
    with open('garbled_email.pickle', 'rb') as fd:
        big_tree = pickle.load(fd)

print >> sys.stderr, "[*] Loaded!"


def all_break2(word):
    trees = [big_tree]
    for c in word:
        ntrees = []
        wordend = False
        for t in trees:
            if c in t:
                ntrees.append( t[c] )
            if '#' in t:
                wordend = True
        if wordend and c in big_tree:
            ntrees.append( big_tree[c] )
        if not ntrees:
            return False
        trees = ntrees
    return bool(sum(1 for t in trees if '#' in t))


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
        if all_break2(sw):
            print sum(1 for c in sw if c == '_')
            break
    else:
        print '!'

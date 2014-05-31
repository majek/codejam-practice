import sys
import string

IN="""
yeqz
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
""".strip()

OUT="""
aozq
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
""".strip()

assert len(IN) == len(OUT)


M = {}
for i, o in zip(IN, OUT):
    if i not in M:
        M[i] = o
    assert M[i] == o
assert set(string.ascii_lowercase) - set(M.keys()) == set()


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    print ''.join(M[c] for c in raw_input())

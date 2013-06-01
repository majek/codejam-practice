import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    t = raw_input()
    last = t[-1].lower()

    print '%s is ruled by %s.' %  (
        t,
        'a queen' if last in 'aeiou'
        else 'nobody' if last in 'y'
        else 'a king')

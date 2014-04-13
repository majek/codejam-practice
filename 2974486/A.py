for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),

    a = input() - 1
    A = [set(raw_input().split()) for _ in range(4)]
    b = input() - 1
    B = [set(raw_input().split()) for _ in range(4)]

    a1, a2, a3, a4 = A[a]

    r = A[a] & B[b]
    if len(r) == 1:
        print list(r)[0]
    elif len(r) > 1:
        print 'Bad magician!'
    else:
        print 'Volunteer cheated!'


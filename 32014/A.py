def collinear((x1, y1), (x2, y2), (x3, y3)):
  return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)

def dist_sq((x0, y0), (x1, y1)):
    return (x0-x1)**2 + (y0-y1)**2

for case_no in xrange(input()):
    x0, y0, x1, y1, x2, y2 = [int(v) for v in raw_input().split()]

    pt = [(x0, y0), (x1, y1), (x2, y2), (x0, y0)]
    a,b,c = sorted([dist_sq(a,b) for a, b in zip(pt[0:-1], pt[1:])])

    if collinear((x0, y0), (x1, y1), (x2, y2)):
        r = 'not a'
    else:
        r = 'isosceles' if a == b or b == c or a == c else \
            'scalene'
        if a + b == c:
            r += ' right'
        elif a + b > c:
            r += ' acute'
        else:
            r += ' obtuse'
    print "Case #%s: %s triangle" % (case_no + 1, r)

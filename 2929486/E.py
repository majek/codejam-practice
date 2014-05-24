import itertools
import sys

print "Case #1:"

data = sys.stdin.read()
o, level, i = [], 0, 0

while i < len(data):
    c2 = data[i:i+2]
    if c2 == '/*':
        level += 1
        i += 2
    elif c2 == '*/' and level > 0:
        level -= 1
        i += 2
    else:
        if level == 0:
            o.append( data[i] )
        i += 1

print ''.join(o)


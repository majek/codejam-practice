'''
Idea taken from this discussion:
https://groups.google.com/group/google-code/browse_thread/thread/a62ddc8aa2fe8b5e/4b8d8553eccc7871?#4b8d8553eccc7871
'''

from bisect import bisect_left

# Longest increasing sequence
def lis(seq):
    inc_seq = []
    for e in seq:
        pos = bisect_left(inc_seq, e)
        if pos >= len(inc_seq):
            inc_seq.append( e )
        else:
            inc_seq[pos] = e
    return inc_seq

lis_count = lambda seq: len(lis(seq))

def solve(names, values, dd):
    assert len(names) == len(values)
    dont_touch = lis_count(values)
    if dont_touch == len(values):
        return []
    for name in sorted(names):
        small_names = names[:]
        small_names.remove( name )
        small_values = values[:]
        small_values.remove( dd[name] )
        if lis_count(small_values) == dont_touch:
            return [name] + solve(small_names, small_values, dd)

for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),

    names  = raw_input().split()
    values = [int(p) for p in raw_input().split()]
    print ' '.join(solve(names, values, dict(zip(names, values))))

import sys
import collections
import math
import itertools

all_combinations = lambda a: itertools.chain(*(itertools.combinations(a, l)
                                               for l in range(1,len(a)+1)))

Store = collections.namedtuple("Store", ["x", "y", "cost"])

def dist(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def solve(a, shopping, whf):
    if not shopping:
        return distances[a][0]
    rmin = Ellipsis
    for item in shopping:
        to_buy = set((item,))
        is_per = bool(to_buy & perishable)
        rem_shopping = shopping - to_buy

        for s in shops_selling[item]:
            cost = distances[a][s] + stores[s].cost[item]
            whf2 = whf
            if is_per:
                if s not in whf:
                    cost += distances[s][0]
                    whf2 |= set((s,))
                    s = 0
                else:
                    cost -= distances[a][s]
                    s = a
            r = cost + solve(s, rem_shopping, whf2)
            rmin = min(rmin, r)
    return rmin


for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    _, num_stores, price_of_gas = map(int, raw_input().split())
    shopping = raw_input().split()

    perishable = set()
    for i in xrange(len(shopping)):
        if shopping[i][-1] == '!':
            shopping[i] = shopping[i][:-1]
            perishable |= set([shopping[i]])

    stores = [Store(0, 0, {})]
    shops_selling = collections.defaultdict(set)
    for i in range(1, num_stores+1):
        l = raw_input().split()
        x_pos, y_pos = map(int, l[:2])
        has = {}
        for ip in l[2:]:
            item, price = ip.split(':')
            if item not in shopping: continue
            has[item] = int(price)
            shops_selling[item].add( i )
        stores.append( Store(x_pos, y_pos, has) )

    distances = [[None] * len(stores) for _ in range(len(stores))]
    for a in range(len(stores)):
        for b in range(a, len(stores)):
            distances[a][b] = distances[b][a] = \
                dist(stores[a], stores[b]) * price_of_gas

    print '%.7f' % (solve(0, frozenset(shopping), frozenset()),)

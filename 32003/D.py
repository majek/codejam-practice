import sys
import collections
import math
import itertools

all_combinations = lambda a: itertools.chain(*(itertools.combinations(a, l)
                                               for l in range(1,len(a)+1)))


Store = collections.namedtuple("Store", ["no", "x", "y", "has", "itemnames"])

def dist(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def count_cost((p,d)):
    if p is None:
        return Ellipsis
    return p + d*price_of_gas

def count_add((p,d), (a, b)):
    return (p+a, d+b)

def solve(a, b, cost, shopping, unvisited_stores, to_buy):
    # Visit b and buy to_buy
    unvisited_stores = unvisited_stores - set((b,))
    shopping = shopping - to_buy
    cost = count_add(cost,
                     (sum(stores[b].has[item] for item in to_buy), distances[a][b]))
    if to_buy & perishable:
        cost = count_add(cost, (0, distances[b][0]))
        b = 0

    if not shopping:
        return count_add(cost, (0, distances[b][0]))

    rets = [(None, None)]
    for c in unvisited_stores:
        to_buy = shopping & stores[c].itemnames
        if not to_buy:
            continue
        for tb in all_combinations(list(to_buy)):
            rets.append( solve(b, c, cost, shopping, unvisited_stores, set(tb)) )
    return min(rets, key=lambda c:count_cost(c))


for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    _, num_stores, price_of_gas = map(int, raw_input().split())
    shopping = raw_input().split()

    perishable = frozenset()
    for i in xrange(len(shopping)):
        if shopping[i][-1] == '!':
            shopping[i] = shopping[i][:-1]
            perishable = perishable | set([shopping[i]])

    shopping = frozenset(shopping)

    stores = [Store(0, 0, 0, {}, set())]
    for i in range(1, num_stores+1):
        l = raw_input().split()
        x_pos, y_pos = l[:2]
        has = {}
        for ip in l[2:]:
            item, price = ip.split(':')
            if item not in shopping: continue
            has[item] = int(price)
        stores.append( Store(i, int(x_pos), int(y_pos), has, set(has.keys())) )

    distances = [[None] * len(stores) for _ in range(len(stores))]
    for a in range(len(stores)):
        for b in range(a, len(stores)):
            distances[a][b] = distances[b][a] = \
                dist(stores[a], stores[b])
    c = solve(0, 0, (0,0), shopping, frozenset(range(1, len(stores))), set())
    print '%.7f' % (count_cost(c),)

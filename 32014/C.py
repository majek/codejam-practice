from collections import defaultdict

def take(city, graph, visited, path_so_far):
    visited = visited.copy()
    r = []
    for road in graph[city]:
        if road in visited:
            continue
        visited[road] = True

        time, city1, city2, i = road
        path_so_far_new = path_so_far + [road]
        r.append( path_so_far_new )
        for one_of_the_roads in take(city2, graph, visited, path_so_far_new):
            r.append( one_of_the_roads )
    return r

def flatten(paths):
    dst = defaultdict(lambda:defaultdict(list))
    for p in paths:
        a = p[0][2]
        b = p[-1][2]
        cost = sum((c for c, _, v, _ in p))
        dst[b][cost].append( p )

    routes_prob = defaultdict(lambda:0)
    city_prob = 1. / len(dst)
    for b, costs in dst.iteritems():
        min_cost = min(costs.iterkeys())
        paths = costs[min_cost]
        prob = city_prob / len(paths)
        for path in paths:
            for road in path:
                routes_prob[road] += prob
    return routes_prob

for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    num_roads, start_city = raw_input().split()
    num_roads = int(num_roads)

    graph = defaultdict(list)
    for i in range(num_roads):
        city1, city2, time = raw_input().split()
        if city2 == start_city:
            # Ignore routes going back to sq 1
            continue
        time = int(time)
        graph[city1].append( (time, city1, city2, i) )

    for roads in graph.values():
        roads.sort() # sort inline

    x = take(start_city, graph, {}, [])
    roads = flatten(x)
    roads = defaultdict(lambda:0., [(i, v) for (_,_,_,i),v in roads.iteritems() ])
    print ' '.join(['%.7f' % (roads[i],)for i in range(num_roads)])

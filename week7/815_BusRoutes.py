from collections import deque, defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        route_table = defaultdict(list)
        for id, route in enumerate(routes):
            for stop in route:
                route_table[stop].append(id)
        
        visited_routes = [False] * len(routes)
        visited_stops = set([source])

        dq = deque([source])
        ans = 0

        while dq:
            ans += 1
            for i in range(len(dq)):
                cur_stop = dq.popleft()
                for route_id in route_table[cur_stop]:
                    if visited_routes[route_id]:
                        continue
                    else:
                        visited_routes[route_id] = True
                        for stop in routes[route_id]:
                            if stop == target:
                                return ans
                            else:
                                if stop not in visited_stops:
                                    dq.append(stop)
                                    visited_stops.add(stop)
        return -1

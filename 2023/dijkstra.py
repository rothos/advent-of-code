import heapq

def shortest_path(start, end):
    seen = set()
    queue = [(0, (start, [start]))]
    while queue:
        cost, (node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            if node == end:
                return path
            for neighbor in neighbors(node):
                heapq.heappush(queue, (cost + 1, (neighbor, path + [neighbor])))

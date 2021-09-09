from heapq import heappush, heappop # Implement priority queue

def neighbors(n,posx,posy):
    directions = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
    visitable = []
    for [v1, v2] in directions:
        if posx + v1 < n and 0 <= posx + v1 and posy + v2 < n and 0 <= posy + v2:
            visitable.append([posx+v1, posy+v2])
    return visitable

def Dijkstra(n, source, target):
    dist = [[None for _ in range(0,n)] for _ in range(0,n)] # Unknown distance from the source vertex to the vertex (i,j)
    prev = [[None for _ in range(0,n)] for _ in range(0,n)] # Predecessor of vertex in optimal path

    # Create vertex priority queue
    candidates = [(0, source)]

    while len(candidates) > 0:
        path_len, [v1,v2] = heappop(candidates)
        if [v1,v2] == target:
            return path_len, prev
        if dist[v1][v2] is None: # This means that v is unvisited
            dist[v1][v2] = path_len
            for [w1,w2] in neighbors(n,v1,v2):
                if dist[w1][w2] is None:
                    prev[w1][w2] = [v1,v2]
                    heappush(candidates, (path_len + 1, [w1,w2]))
    return -1  # If it completed the While loop and didn't return anything then it couldn't have reached the target.

def readPath(prev, source, target):
    [c1,c2] = target
    path = [target]
    while [c1,c2] != source:
        [c1,c2] = prev[c1][c2]
        path.append([c1,c2])
    return path[::-1]

# Save all of the paths
def allPaths(n):
    paths = []
    paths = [[[[None for _ in range(0,n)] for _ in range(0,n)]for _ in range(0,n)] for _ in range(0,n)]
    for i in range(0,n):
        for j in range(0, n):
            for k in range(0,n):
                for l in range(0,n):
                    dist, prev = Dijkstra(n, [i,j], [k,l])
                    paths[i,j,k,l] = readPath(prev, [i,j], [k,l])
    return paths


def badPaths(n):
    bad_paths = []
    paths = [[[[None for _ in range(0,n)] for _ in range(0,n)]for _ in range(0,n)] for _ in range(0,n)]
    for i in range(0,n):
        for j in range(0, n):
            for k in range(0,n):
                for l in range(0,n):
                    if Dijkstra(n, [i,j], [k,k]) == -1:
                        bad_paths.append([i, j, k, l])
    return bad_paths


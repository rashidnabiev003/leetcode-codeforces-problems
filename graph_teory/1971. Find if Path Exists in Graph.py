n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 3
destination = 9

from collections import defaultdict

s = defaultdict(list)
for i, j in edges:
    s[i].append(j)
    s[j].append(i)

visited = set()
def dfs(graph, node, visited):
    visited.add(node)
    for i in graph[node]:
        if i not in visited:
            dfs(graph, i, visited)

dfs(s, source, visited)

if destination in visited:
    print(True)
else:
    print(False)
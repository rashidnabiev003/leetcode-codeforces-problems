graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()         # берём верхний элемент
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)  # кладём соседей на стек
    return visited

def dfs(graph, node, visited):
    visited.add(node)           # 1. Отметь: "я тут был"
    for neighbor in graph[node]: # 2. Посмотри на всех соседей
        if neighbor not in visited:  # 3. Если сосед ещё не посещён
            dfs(graph, neighbor, visited)  # 4. Иди в него (рекурсия!)

visited = set()
dfs(graph, 0, visited)
print(visited)


from collections import deque

def bfs_shortest(graph, start, target):
    visited = {start}
    queue = deque([(start, 0)])  # (вершина, расстояние)

    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist            # нашли! это гарантированно кратчайший

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # путь не найден



from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])       # очередь вместо стека!
    
    while queue:
        node = queue.popleft()   # берём ПЕРВЫЙ (не последний!)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
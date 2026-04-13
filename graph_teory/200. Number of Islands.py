grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# Вот так ты "ходишь" по соседям клетки (row, col):
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#              вправо  влево    вниз    вверх

row, col = 2, 2  # текущая клетка
for dr, dc in directions:
    nr, nc = row + dr, col + dc
    # Проверяем что не вышли за границы
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        # (nr, nc) — это сосед!
        print(f"Сосед: ({nr}, {nc}) = {grid[nr][nc]}")

visited = set()

def dfs(grid, row, col, visited):
    visited.add((row, col))   
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dr, dc in directions:           
        nr, nc = row + dr, col + dc  
        
        if (
            0 <= nr < len(grid)            
            and 0 <= nc < len(grid[0])   
            and grid[nr][nc] == "1"   
            and (nr, nc) not in visited 
        ):
            dfs(grid, nr, nc, visited) 

count = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if (row, col) not in visited and grid[row][col] == "1":
            dfs(grid, row, col, visited)
            count +=1
print(count)
      
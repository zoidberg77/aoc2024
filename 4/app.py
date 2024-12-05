def get_directions():
    return [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]

def check_word(grid, row, col, dx, dy, word):
    if not (0 <= row + dx * (len(word)-1) < len(grid) and 
            0 <= col + dy * (len(word)-1) < len(grid[0])):
        return False
    
    return all(grid[row + dx * i][col + dy * i] == word[i] 
              for i in range(len(word)))

def count_word_occurrences(grid, word):
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            for dx, dy in get_directions():
                if check_word(grid, row, col, dx, dy, word):
                    count += 1
    
    return count

def check_xmas_pattern(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    

    if (row + 1 >= rows or 
        col + 1 >= cols or 
        col - 1 < 0 or
        row - 1 < 0):
        return False
    

    if grid[row][col] != 'A':
        return False
        
    ul = grid[row-1][col-1]
    ur = grid[row-1][col+1]
    ll = grid[row+1][col-1]
    lr = grid[row+1][col+1]
    
    diag1 = [ul + grid[row][col] + lr, lr + grid[row][col] + ul]  
    diag2 = [ur + grid[row][col] + ll, ll + grid[row][col] + ur] 
    
    return any(d1 in ('MAS', 'SAM') and d2 in ('MAS', 'SAM') and d1 != d2 
              for d1 in diag1 for d2 in diag2)

def count_xmas_patterns(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if check_xmas_pattern(grid, row, col):
                count += 1
    
    return count


with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

part1 = count_word_occurrences(grid, "XMAS")
print(f"Part 1: {part1}")

part2 = count_xmas_patterns(grid)
print(f"Part 2: {part2}")

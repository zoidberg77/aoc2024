def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def find_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((y2-y1) * (x3-x1) - (y3-y1) * (x2-x1)) < 1e-10

def calculate_antinodes(grid, antennas):
    antinodes = set()
    height = len(grid)
    width = len(grid[0])
    
    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue
            
        for y in range(height):
            for x in range(width):
                point = (x, y)
                
                for i, pos1 in enumerate(positions):
                    for pos2 in positions[i+1:]:
                        if is_collinear(pos1, pos2, point):
                            antinodes.add(point)
                            break
                    else:
                        continue
                    break
    
    return len(antinodes)

def solve(filename):
    grid = read_input(filename)
    antennas = find_antennas(grid)
    return calculate_antinodes(grid, antennas)

print(solve('input.txt'))
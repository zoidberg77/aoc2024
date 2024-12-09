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

def distance(p1, p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

def find_antinode(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    
    x3 = x1 + dx * 2
    y3 = y1 + dy * 2
    
    x4 = x2 - dx * 2
    y4 = y2 - dy * 2
    
    return [(int(x3), int(y3)), (int(x4), int(y4))]

def calculate_antinodes(grid, antennas):
    antinodes = set()
    height = len(grid)
    width = len(grid[0])
    
    for freq, positions in antennas.items():
        for i, pos1 in enumerate(positions):
            for pos2 in positions[i+1:]:
                for antinode in find_antinode(pos1, pos2):
                    x, y = antinode
                    if 0 <= x < width and 0 <= y < height:
                        if is_collinear(pos1, pos2, antinode):
                            d1 = distance(pos1, antinode)
                            d2 = distance(pos2, antinode)
                            if abs(d1/d2 - 2.0) < 1e-10 or abs(d2/d1 - 2.0) < 1e-10:
                                antinodes.add(antinode)
    
    return len(antinodes)

def solve(filename):
    grid = read_input(filename)
    antennas = find_antennas(grid)
    return calculate_antinodes(grid, antennas)

print(solve('input.txt'))
import numpy as np
from tqdm import trange

def load_map(filename):
    play_map = []
    with open(filename) as f:
        for line in f.readlines():
            l = [x for x in line.strip()]
            play_map.append(l)
    return np.array(play_map)

class Guard:
    def __init__(self):
        self.pos = (0, 0)
        self.visited = set()
        self.orientation = '^'
        self.path = []

def check_bounds(x, y, play_map):
    return 0 <= x < play_map.shape[0] and 0 <= y < play_map.shape[1]

def simulate_guard_movement(play_map):
    guard_pos = np.where(play_map == '^')
    guard = Guard()
    guard.pos = (guard_pos[0][0], guard_pos[1][0])
    guard.orientation = '^'
    guard.visited.add(guard.pos)
    
    movements = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    next_orientation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    while True:
        movement = movements[guard.orientation]
        new_pos = (guard.pos[0] + movement[0], guard.pos[1] + movement[1])
        
        if not check_bounds(new_pos[0], new_pos[1], play_map):
            break
            
        if play_map[new_pos] == '#':
            guard.orientation = next_orientation[guard.orientation]
            continue
            
        guard.pos = new_pos
        guard.visited.add(new_pos)
    
    return len(guard.visited)

def simulate_guard_movement2(play_map):
    guard_pos = np.where(play_map == '^')
    guard = Guard()
    guard.pos = (guard_pos[0][0], guard_pos[1][0])
    guard.orientation = '^'
    
    movements = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    next_orientation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    visited_states = set()
    state_sequence = []
    
    while True:
        current_state = (guard.pos, guard.orientation)
        
        if current_state in visited_states:
            loop_start = state_sequence.index(current_state)
            if loop_start < len(state_sequence) - 1:
                return True
        
        if len(state_sequence) > play_map.size * 4:
            return False
            
        visited_states.add(current_state)
        state_sequence.append(current_state)
        
        movement = movements[guard.orientation]
        new_pos = (guard.pos[0] + movement[0], guard.pos[1] + movement[1])
        
        if not check_bounds(new_pos[0], new_pos[1], play_map):
            return False
            
        if play_map[new_pos] == '#':
            guard.orientation = next_orientation[guard.orientation]
            continue
            
        guard.pos = new_pos

play_map = load_map('input.txt')
result = simulate_guard_movement(play_map)
print(f"Part 1: The guard visited {result} distinct positions")

play_map = load_map('input.txt')
obs_count = 0

for x in trange(play_map.shape[0]):
    for y in range(play_map.shape[1]):
        if play_map[x][y] in ['^', '#']:
            continue
        
        test_map = play_map.copy()
        test_map[x][y] = '#'
        
        if simulate_guard_movement2(test_map):
            obs_count += 1

print(f"Part 2: Found {obs_count} positions that create loops")
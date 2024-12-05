from collections import defaultdict, deque

def parse_input():
    with open('input.txt', 'r') as file:
        rules_section, updates_section = file.read().strip().split('\n\n')
    
    rules = set()
    for line in rules_section.split('\n'):
        before, after = map(int, line.split('|'))
        rules.add((before, after))
    
    updates = []
    for line in updates_section.split('\n'):
        pages = list(map(int, line.strip().split(',')))
        updates.append(pages)
    
    return rules, updates

def is_valid_order(pages, rules):
    for i, page in enumerate(pages):
        for next_page in pages[i+1:]:
            if (next_page, page) in rules:
                return False
    return True

def get_middle_value(pages):
    return pages[len(pages)//2]

def create_graph(pages, rules):
    graph = defaultdict(set)
    indegree = defaultdict(int)
    nodes = set(pages)
    
    for before, after in rules:
        if before in nodes and after in nodes:
            graph[before].add(after)
            indegree[after] += 1
            if before not in indegree:
                indegree[before] = 0
    
    return graph, indegree

def topological_sort(pages, rules):
    graph, indegree = create_graph(pages, rules)
    queue = deque([node for node in pages if indegree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

def solve():
    rules, updates = parse_input()
    part1_total = 0
    part2_total = 0
    
    for update in updates:
        if is_valid_order(update, rules):
            middle = get_middle_value(update)
            part1_total += middle
        else:
            sorted_update = topological_sort(update, rules)
            middle = get_middle_value(sorted_update)
            part2_total += middle
    
    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")

solve()
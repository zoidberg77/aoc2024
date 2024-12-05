def is_safe(levels):
    if len(levels) <= 1:
        return False

    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    all_positive = all(diff > 0 for diff in diffs)
    all_negative = all(diff < 0 for diff in diffs)
    
    if not (all_positive or all_negative):
        return False
        
    return all(1 <= abs(diff) <= 3 for diff in diffs)

def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True
    
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe(dampened_levels):
            return True
    return False

def count_safe_reports(input_data):
    safe_count = 0
    safe_with_dampener_count = 0
    
    for line in input_data.strip().split('\n'):
        levels = [int(x) for x in line.strip().split()]
        if is_safe(levels):
            safe_count += 1
            safe_with_dampener_count += 1
        elif is_safe_with_dampener(levels):
            safe_with_dampener_count += 1
            
    return safe_count, safe_with_dampener_count

txt_input = ''

with open('input.txt', 'r') as f:
    txt_input = f.read()

regular_safe, dampener_safe = count_safe_reports(txt_input)
print(f"Number of safe reports (without dampener): {regular_safe}")
print(f"Number of safe reports (with dampener): {dampener_safe}")
import re

def process_memory(content):
    pattern = r'(?:mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    total = 0
    enabled = True
    
    matches = re.finditer(pattern, content)
    for match in matches:
        full_match = match.group(0)
        
        if full_match == 'do()':
            enabled = True
        elif full_match == "don't()":
            enabled = False
        elif enabled:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            result = num1 * num2
            total += result
        
    return total

with open('input.txt', 'r') as f:
    memory_content = f.read()

part1_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
part1_total = sum(int(match.group(1)) * int(match.group(2)) 
                 for match in re.finditer(part1_pattern, memory_content))

part2_total = process_memory(memory_content)

print(f"Part 1 - Sum of all multiplication results: {part1_total}")
print(f"Part 2 - Sum of enabled multiplication results: {part2_total}")
from itertools import product

def parse_line(line):
    test_value, numbers = line.split(': ')
    return int(test_value), [int(x) for x in numbers.split()]

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        else:
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_make_value(test_value, numbers, include_concat=False):
    if len(numbers) == 1:
        return test_value == numbers[0]
    
    operators = ['+', '*'] if not include_concat else ['+', '*', '||']
    
    num_operators = len(numbers) - 1
    for ops in product(operators, repeat=num_operators):
        try:
            if evaluate_expression(numbers, ops) == test_value:
                return True
        except (ValueError, OverflowError):
            continue
    return False

def solve_calibration(data, include_concat=False):
    total = 0
    for line in data.strip().split('\n'):
        test_value, numbers = parse_line(line)
        if can_make_value(test_value, numbers, include_concat):
            total += test_value
    return total

with open('7.txt', 'r') as file:
    input_data = file.read()

result_part1 = solve_calibration(input_data, include_concat=False)
print(f"Part 1 - Total calibration result: {result_part1}")

result_part2 = solve_calibration(input_data, include_concat=True)
print(f"Part 2 - Total calibration result: {result_part2}")
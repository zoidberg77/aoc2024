import pandas as pd


first_numbers = []
second_numbers = []

with open('input.tsv', 'r') as file:
    for line in file:
        # Split each line into two numbers and convert to integers
        num1, num2 = map(int, line.strip().split())
        first_numbers.append(num1)
        second_numbers.append(num2)
        
first_numbers = sorted(first_numbers)
second_numbers = sorted(second_numbers)

dist = 0
for i, j in zip(first_numbers, second_numbers):
    dist += abs(i-j)

print(dist)

counts = {}

for i in first_numbers:
    if str(i) not in counts.keys():
        counts[str(i)] = 0
    for j in second_numbers:
        if i==j:
            counts[str(i)]+=1
        elif j>i:
            break

for k in counts.keys():
    counts[k] = int(k)*counts[k]

sum_counts = [i for i in counts.values()]
print(sum(sum_counts))
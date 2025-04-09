from itertools import combinations

intg = int(input())
litters = list(map(str,input().split()))
combination_number = int(input())
count = 0
total = 0
for c in combinations(litters,combination_number):
    if "a" in c :
        count += 1
    total += 1
result = (count/total)
print(f'{result:.4f}')
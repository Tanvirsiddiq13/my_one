import sys
set_a = set(list(map(int,input().split())))
n = int(input())
for i in range(n):
    set_n = set(list(map(int,input().split())))
    if not set_a.issuperset(set_n):
        print(False)
        sys.exit(0)
print(True)
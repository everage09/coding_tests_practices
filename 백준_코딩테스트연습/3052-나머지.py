import sys

s = []
for _ in range(10):
    data = int(input())
    s.append(data%42)

print(len(set(s)))

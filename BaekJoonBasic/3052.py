s = set()
for i in range(10):
    num = int(input())
    num %= 42
    s.add(num)

sum = 0

for j in s:
    sum += 1

print(sum)
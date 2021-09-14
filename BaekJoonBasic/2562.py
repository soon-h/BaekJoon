big = 0
count = 0
for i in range(9):
    num = int(input())
    if num > big:
        big = num
        count = i + 1
    else:
        pass

print(big)
print(count)
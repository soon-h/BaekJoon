num = int(input())
a = list(map(int,input().split()))


small = a[0]
big = a[0]
for j in range(num):
    if a[j] < small:
        small = a[j]
    if a[j] > big:
        big = a[j]

print(small,big)
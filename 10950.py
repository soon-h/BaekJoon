num = int(input())
sum = []

for i in range(num):
    x,y = input().split()
    x = int(x)
    y = int(y)
    add = x + y
    sum.append(add)

for j in range(num):
    print(sum[j])

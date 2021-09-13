import sys
num = int(input())
sum = 0
show = []
for i in range(num):
    x , y = map(int,sys.stdin.readline().split())
    sum = x + y
    show.append(sum)

for j in range(num):
    print("Case #{}: {}".format(j+1,show[j]))
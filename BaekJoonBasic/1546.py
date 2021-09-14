num = int(input())

scores = list(map(int,input().split()))

scores.sort()

biggest = scores[num - 1]
answer = 0

for i in range(num):
    answer += scores[i]/biggest*100

print(answer/num)
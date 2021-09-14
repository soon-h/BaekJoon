num = int(input())
ox = []
sum = 0
answer = 0
for i in range(num):
    seperox = list(input())
    ox.append(seperox)

for j in range(num):
    for k in range(len(ox[j])):
        if ox[j][k] == "O":
            sum += 1
            answer += sum
        if ox[j][k] == "X":
            if sum > 0:
                sum = 0
            else:
                pass
    print(answer)
    answer = 0
    sum = 0
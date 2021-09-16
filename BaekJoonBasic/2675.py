howmay = int(input())

for i in range(int(howmay)):
    num,word = input().split()
    answer = ""
    for j in word:
        answer += int(num) * j
    print(answer)
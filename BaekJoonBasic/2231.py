num = int(input())
result = 0

for i in range(1, num+1):        # 1 부터 n 까지
    n = list(map(int, str(i)))   # 각 자리수를 분해
    s = i + sum(n)               # 분해합을 구함
    if(s == num):                # 분해합이 n 과 같다면
        result = i               # result = i , 종료
        break

print(result)                    # 생성자 출력
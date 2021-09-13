num = int(input())
start = num
sum = 0
while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    sum += 1
    if start == num:
        print(sum)
        break
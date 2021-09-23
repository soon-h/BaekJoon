howmany = int(input())

for i in range(howmany):
    start , end = map(int,input().split())
    distance = end - start
    count = 0
    move = 1
    nowdis = 0
    while nowdis < distance:
        count += 1
        nowdis += move
        if count % 2 == 0:
            move += 1
    print(count)
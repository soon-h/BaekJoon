while True:
    x = list(map(int,input().split()))
    if sum(x)== 0:
        break
    max_num = max(x)
    x.remove(max_num)
    if x[0] ** 2 + x[1] ** 2 == max_num ** 2:
        print("right")
    else:
        print("wrong")    
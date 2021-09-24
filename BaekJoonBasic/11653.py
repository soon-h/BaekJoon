num = int(input())
div = 2
div_list = []

if num == 1:
    print()
else:
    while div <= num:
        if num % div == 0:
            div_list.append(div)
            num = num / div
        else :
            div += 1

    div_list.sort()
    
    for i in div_list:
        print(i)
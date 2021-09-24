num = int(input())
numbers = map(int, input().split())
count = 0
for i in numbers:
    dvi = 0
    if i > 1 :
        for j in range(2, i):  
            if i % j == 0:
                dvi += 1 
        if dvi == 0:
            count += 1  
print(count)
Hour,Min = input().split()
Hour = int(Hour)
Min = int(Min)

if Min < 45:
    if Hour == 0:
        Hour = 23
        Min = 60 - (45 - Min)
        print(Hour,Min)
    else:
        Hour -= 1
        Min = 60 - (45 - Min)
        print(Hour,Min)
else:
    Min -= 45
    print(Hour,Min)
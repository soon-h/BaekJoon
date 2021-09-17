from typing import Counter


A , B , C = map(int,input().split())
i = 1

while True:
    if B >= C:
        print("-1")
        break
    
    if A + (B * i) == C * i:
        print(i + 1)
        break
    else:
        i += 1
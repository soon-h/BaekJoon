text = list(map(str,input()))

alpa = []

for k in range(26):
    alpa.append(0)

for i in text:
    for j in range(97,123):
        if i == chr(j):
            alpa[122 - j] = int(alpa[122 - j]) + 1
        else:
            pass

alpa.reverse()

for o in range(26):
    if alpa[o] == 0:
        alpa[o] = -1

for h in range(26):
    if alpa[h] != 0 and alpa[h] != -1:
        alpa[h] = text.index(chr(97 + h))


for n in range(26):
    print(str(alpa[n])+" ",end="")
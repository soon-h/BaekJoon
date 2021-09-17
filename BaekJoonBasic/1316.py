repeatnum = int(input())
answer = repeatnum

for i in range(repeatnum):
    text = input()
    for j in range(len(text) - 1):
        if text[j] == text[j+1]:
            pass
        elif text[j] in text[j+1:]:
            answer -= 1
            break
print(answer)
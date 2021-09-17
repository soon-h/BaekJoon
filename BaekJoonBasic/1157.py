# text = input().upper()
# new_text = text
# sum = 0
# st = 0
# a = []

# for i in range(len(text)):
#     for j in range(i ,len(new_text)):
#         if text[i] == new_text[j]:
#             a.append(text[i])
#             a.append(text.count(text[i]))
#             new_text = new_text.replace(text[i]," ")

        
        
# for k in range(len(a)):
#     if k != 0 and k % 2 != 0:
#         if a[k] == sum:
#             print("?")
#             break

#         if k != len(a) - 1 and a[k] > sum:
#             sum = a[k]
#             st = k
        
#         if  k == len(a) - 1 and a[k] > sum:
#             print(a[k - 1])
#             break
#         if k == len(a) - 1:
#             print(a[st - 1])

text = input().upper()
text_set = list(set(text))
arr = []
for i in text_set:
    arr.append(text.count(i))

if arr.count(max(arr)) > 1:
    print("?")
else:
    print(text_set[arr.index(max(arr))])

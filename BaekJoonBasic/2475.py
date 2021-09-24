nums = list(map(int,input().split()))
gomnum = 0
for num in nums:
    gomnum += num* num
print("{}".format(gomnum % 10))
start = int(input())
end = int(input())
sosu_list = []

for snum in range(start,end + 1):
    divcount = 0
    if snum > 1:
        for divnum in range(2,snum):
            if snum % divnum == 0:
                divcount += 1
                break
        if divcount == 0:
            sosu_list.append(snum)

if len(sosu_list) > 0:
    print("{}\n{}".format(sum(sosu_list),min(sosu_list)))
else:
    print(-1)
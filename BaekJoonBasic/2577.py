a = []
for i in range(3):
    num = int(input())
    a.append(num)

sum = a[0] * a[1] * a[2]

b = list(map(int,str(sum)))

print("{}".format(b.count(0)))
print("{}".format(b.count(1)))
print("{}".format(b.count(2)))
print("{}".format(b.count(3)))
print("{}".format(b.count(4)))
print("{}".format(b.count(5)))
print("{}".format(b.count(6)))
print("{}".format(b.count(7)))
print("{}".format(b.count(8)))
print("{}".format(b.count(9)))
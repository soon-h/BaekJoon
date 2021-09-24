dajangjo = list(map(int,input().split()))

if dajangjo == sorted(dajangjo):
    print('ascending')
elif dajangjo == sorted(dajangjo, reverse=True):
    print('descending')
else:
    print('mixed')
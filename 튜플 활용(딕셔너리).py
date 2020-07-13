d=dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
    print(k,v)
tups=d.items()
print(tups)

#여러 값에 대해 비교
print((0,1,2)<(5,1,2))
print((0,1,200000)<(0,3,4))
print(('Jones','Sally')<('Jones','Sam'))
print(('Jones','Sally')<('jones','Sam'))
print(('Jones','Sally')>('Adams','Sam'))

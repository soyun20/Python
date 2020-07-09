counts=dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name in counts:
        counts[name]=counts[name]+1
    else:
        counts[name]=1
print(counts)


counts=dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

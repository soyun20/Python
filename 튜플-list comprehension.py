c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
tmp=sorted(tmp)
print(tmp)

c={'a':10,'b':1,'c':22}
print(sorted([(v,k)for k,v in c.items()]))

name = input("Enter file:")
handle = open(name)
lst=list()
count=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        time=words[5]
        a=time.find(':')
        hours=time[:a]
        hours=hours.split()
        for hour in hours:
            count[hour]=count.get(hour,0)+1
for k,v in count.items():
    kv=(k,v)
    lst.append(kv)
    lst=sorted(lst)
for k,v in lst:
    print(k,v)

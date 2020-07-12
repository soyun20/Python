name = input("Enter file:")
handle = open(name)
bigcount=None
bigword=None
emaildict=dict()
for line in handle:
    if line.startswith('From '):
        line.split()
        a=line.find(' ')
        b=line.find(' ',a+1)
        words=line[a+1:b]
        words.split()
        emaildict[words]=emaildict.get(words,0)+1
for word,count in emaildict.items():
    if bigcount is None or bigcount<count:
        bigword=word
        bigcount=count
print(bigword,bigcount)

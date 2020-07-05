# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s=0.0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        b=line.find(':')
        a=line[b+1:]
        a=float(a)
        s+=a
        count+=1
f=float(s/count)
print('Average spam confidence:',f)

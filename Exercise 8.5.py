fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    line.split()
    if len(line) > 1:
        if line.startswith('From:'):
            a=line.find(':')
            email=line[a+1:]
            email=email.strip()
            print(email)
            count+=1
print("There were", count, "lines in the file with From as the first word")

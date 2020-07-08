fname = input("Enter file name: ")
fh = open(fname)
lst=list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)

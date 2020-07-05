fname=input('Enter the file name: ')
try:
    a = open(fname)
except:
    print('File cannot be opened',fname)
    quit()
count=0
for line in a:
    if line.startswith('Subject:'):
        count+=1
print('There were',count,'subject lines in',fname)

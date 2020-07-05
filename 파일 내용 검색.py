a = open('hello.txt')
for line in a:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)

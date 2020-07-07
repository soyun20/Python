line = 'Form stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008'
a=line.split()
print(a[1])
email=a[1]
address= email.split('@')
print(address)
print(address[1])

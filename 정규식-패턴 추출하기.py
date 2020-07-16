import re
x='My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)

x='From: Using the : character'
y=re.findall('^F.+:',x)
print(y)
y=re.findall('^F.+?:',x)
print(y)

x='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('\S+@\S+',x)
print(y)
y=re.findall('^From(\S+@\S+)',x)
print(y)

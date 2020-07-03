largest=-1
print('Before',largest)
numbers=[9,41,12,3,74,15]
for number in numbers:
  if number>largest:
    largest=number
  print('largest:',largest,'number:',number)
print('After',largest)

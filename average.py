count=0
sum=0
print('Before',count,sum)
numbers=[9,41,12,3,74,15]
for value in numbers:
  count=count+1
  sum=sum+value
  print(count,sum,value)
print('After',count,sum,sum/count)

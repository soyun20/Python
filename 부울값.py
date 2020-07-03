found= False
print('Before',found)
numbers=[9,41,12,3,74,15]
for value in numbers:
    if value==3:
        found=True
        print(found,value)
        break
print('After',found)

largest = None
smallest = None
num = None
while num!="done":
    num = input("Enter a number: ")
    try:
        num=int(num)
        if largest == None:
            largest=num
        elif largest<num:
            largest=num

        if smallest == None:
            smallest=num
        elif smallest>num:
            smallest=num
    except:
        if(num!="done"):
        	print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

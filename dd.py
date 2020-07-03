def buildfunction(number):
    if number == 1:
        def functiona():
            print ("i am functiona")
        functiona()
    else:
        def functionb():
            print("i am functionb")
        functionb()

number = int(input("Enter a number:"))
buildfunction(number)

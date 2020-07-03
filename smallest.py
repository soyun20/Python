smallest=None
print('Before')
numbers=[9,41,12,3,74,15]
for value in numbers:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('After',smallest)

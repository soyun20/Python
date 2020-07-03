x= int(input("x값을 입렵하시오:  "))

if x<2:
    print('Small')
elif x<10:
    print('Medium')
elif x<20:
    print('Big')
elif x<40:
    print('Large')
elif x<100:
    print('Huge')
else:
    print('Ginormous')

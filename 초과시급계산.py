h=input('Enter Hours:  ')
r=input('Enter Rate:  ')
#print(h,r)
while True:
    try:
        fh=float(h)
        fr=float(r)
        if fh>40:
         # print('Overtime')
            reg=fh*fr
            otp=(fh-40.0)*(fr*0.5)
         # print(reg,otp)
            xp=reg+otp
        else:
         # print('regular')
            xp=fh*fr
        print('Pay:',xp)
        break
    except:
        print("Error, please enter numberic input")
        quit()

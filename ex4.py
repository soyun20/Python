def computepay(h,r):
  if h>40:
    reg=h*r
    otp=(h-40.0)*(r*0.5)
    pay=reg+otp
  else:
    pay=h*r
  return pay

fh=float(input('Enter Hours:  '))
fr=float(input('Enter Rate:  '))
xp=computepay(fr,fr)
print("pay",xp)

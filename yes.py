per=int(input('enter your percentage'))
if per>=80 and per<100:
    print('Distinction')
elif per>=70 and per<80:
    print('first division')
elif per>=60 and per<70:
    print('second division')
elif per>=50 and per<60:
    print('third division')
else:
    print('better luck for next time')
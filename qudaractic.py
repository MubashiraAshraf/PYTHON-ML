a = int(input('Enter the coefficient of x^2'))
b = int(input('Enter the coefficient of x'))
c = int(input('Enter the coefficient of x^0'))
k = (b**2)-(4*a*c)
d = k**0.5
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)
print('the roots are',x1,x2)
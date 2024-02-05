# calulate the hypothenuse of a rectangle triangle given the two catheti

# enter the catheti

import cmath

c1= input('enter the first cathetus')
c2= input('enter the second cathetus')

# calculate the hypothenuse

h=cmath.sqrt(float(c1)**2+float(c2)**2)

print('The hipothenuse is {0}'.format(h) )



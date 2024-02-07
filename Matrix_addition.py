X = [[12, 7, 3],
     [4, 5, 6]]

#print(len(X)) # len gives the number of rows
#print(len(X[0])) # gives the number of columns

#--------------------#
 # gives to matrices

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

#r=range(len(X)) #0,1,2 3=len(X) num of rows
#for i in r:
    #print(i)

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

# give matrux of result, now as an empty matrix
import numpy as np
result_add=np.zeros((3,3)) # matrix 3x3 of all zeros

for i in range(len(X)):
    for j in range(len(X[0])):
        result_add[i][j]=X[i][j]+Y[i][j]

print(result_add)

# ------------------- #

result_mul=np.zeros((3,3)) # matrix 3x3 of all zeros

for i in range (len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result_mul[i][j] += X[i][k]*Y[k][j] # += sum the element over k

print(result_mul)

# transpose

r=len((X)) # rows
c=len((X[0])) # cols
import numpy as np
t = np.empty((c,r))
for i in range(c):
    for j in range(r):
          t[i][j]=X[j][i]
print(t)




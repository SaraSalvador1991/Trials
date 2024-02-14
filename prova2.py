import random

x = [1, 4, 6, 8, 11]
for i in reversed(x) : # reverse the list to check from the last to the first component
    print("visits", i)
    if i % 2 == 0:
        print(i)
        x.remove(i) # remove odd elements from the list
print(x)

# -------------

y = [1, 4, 6, 8, 11]
for i in reversed(y) : # reverse the list to check from the last to the first component
    print("visits", i)
    if i % 2 != 0:
        print(i)
        y.remove(i) # remove odd elements from the list
print(y)

# ---------------
# while loop

# Iterate until x becomes 0
x = 6
while x: # untill this is true i.e. untill x is not zero
    print(x)
    x -= 1
# Prints 6 5 4 3 2 1

# ----------------

# return all positive numbers in a list

list = [1,11,-97,-9,-91,97]
for i in reversed(list):
    if i <= 0:
        list.remove(i)
print(list)

# ---

# return all negative numbers in a list

list = [1,11,-97,-9,-91,97]
for i in reversed(list):
    if i > 0:
        list.remove(i)
print(list)

# ------------

#check is an array is monotonic

x = [1,2,3,4,12,11]
n = len(x) # length of the array
if all(x[i]<=x[i+1] for i in range(0,n-1) or x[i]>=x[i+1] for i in range(0,n-1)):
    print('The array is monotonic')
else:
    print('The array is not monotonic')

# -----------

# transpose only a row of a matrix
import numpy as np
M =  [[1, 2],
      [3, 4],
      [5, 6]]
print(M)
r = len(M) # num of rows
c = len(M[0]) # num of col
t = np.empty((c,r)) # empty matrix
for i in range(0,c):
    for j in range(0,r):
        t[i][j]=M[j][i]
print(t)

# -------------

# print second largest number of a list

x = [12,1,100]
max = 0
for i in x:
    if i > max:
        max = i
print(max)
print(x)
x.remove(max)
print(x)

res = 0
for j in x:
    if j > res:
        res = j
print('The second largest is', res)

# if there are negative elements

from functions import my_max
from functions import my_min
from functions import pos
from functions import neg
from functions import MY_MAX
from functions import MY_MIN
x = [3,4,5,1,91]
print(my_max(x)) # ok
print(my_min(x)) # ok
x= [-1,2,-3,4,-5]
#print(pos(x))
print(neg(x))


x = [2,-4,5,-19,-11]

if all(i < 0 for i in x):
    y = [abs(i) for i in x]
    print(-my_min(y))
elif all(i>=0 for i in x):
    print(my_max(x))
else:
    print(my_max(neg(x)))


x = [-10,1,-11,25,-2]
print(MY_MAX(x))
#print(MY_MIN(x))


# -----------

x = [-1,2,11,-4]
max = x[0]
for i in x:
    if i>max:
        max = i
print(max)

min = x[0]
for i in x:
    if i< min:
        min = i
print(min)

# ----------

stringa = ['Casa', 'Gatto', 'Berna', 'Thun']
k = 5
for i in stringa:
    if len(i)==k:
        print(i)

# ----------

# cumulative sum

def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
    return cu_list[1:]


# Driver Code
lists = [10, 20, 30, 40, 50]
print(Cumulative(lists))

s = 0
cumsum = [(s:=s+i) for i in lists]
print(cumsum)


















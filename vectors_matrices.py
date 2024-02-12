array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
array.remove(40) # remove the number 40 from the array (vector)
print(array)

index = 5
array.pop(5) # delete the entrance 5 from the array
print(array)
# ----------------
import numpy as np
a = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
a_del = np.delete(a, 2, 1)
print(a_del)



 read data in csv

import panda as pd
data_cars = pd.read_csv("C:\Users\sara\Desktop\cars.csv") # not working ?

# arrays
# swap first and last exntrance

def swap(list):
    n = len(list)
    t = list[0]
    list[0] = list[n-1]
    list[n-1] = t
    return list

list = [0,1,3,4,5]

print(swap(list))

# ----------------
#x = [1, 4, 6, 8, 11]
#index = 1,2
#x.pop(index)

# print even numbers in a list

x = [1, 4, 5, 8, 11]
for i in x :
    if i % 2 != 0:
        x.remove(i) # remove odd elements from the list
        print(x)

y = [1, 4, 6, 8, 11]
for i in y:
    if i % 2 == 0:
        y.remove(i)  # remove even elements from the list
        print(y)



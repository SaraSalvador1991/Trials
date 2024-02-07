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



# read data in csv

#import panda as pd
#data_cars = pd.read_csv("/Users/sarasalvador/Downloads/cars.csv") # not working ?



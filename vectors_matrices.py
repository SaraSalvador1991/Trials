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
for i in reversed(x) :
    if i % 2 != 0:
        x.remove(i) # remove odd elements from the list
print(x)

y = [1, 4, 6, 8, 11]
for i in reversed(y):
    if i % 2 == 0:
        y.remove(i)  # remove even elements from the list
print(y)


# Write a Python program to insert a newly created item before the second element in an existing array

import numpy as np
x = [1, 3, 5, 7, 9]
x.insert(1,4)
print(x)


#Write a Python program to find the first duplicate element in a given array of integers. Return -1 if there are no such elements.

def find_first_duplicate(nums):
    num_set = set() #start empty set
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set: # if the element is not in the set add it. the first time an element is already in the set it prints it
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
print(find_first_duplicate([1, 2, 3, 4]))
print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))

# Write a Python program to find out if a given array of integers contains any duplicate elements.
# Return true if any value appears at least twice in the array, and return false if every element is distinct.

x = [1, 2, 3, 4, 5, 11]
if all(x.count(i) == 1 for i in x):
    print('False')
else:
    print('True')



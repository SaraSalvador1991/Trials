x = [1, 4, 6, 8, 11]
for i in x :
    if i % 2 == 0: # 6 not displayed ?
        print(i)
        x.remove(i) # remove odd elements from the list
print(x)

# -----------------

# cumulative sum

y= [-11,2,3]
c_sum = 0
for i in y:
    c_sum +=i # okk :)
print(c_sum)

# -------------
# print kth column of matrix

import numpy as np
# initialize list
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
# printing original list
print("The original list is : " + str(test_list))
#initialize K
K = 2
# Get Kth Column of Matrix
# using numpy
res = np.array(test_list)[:,K]
# printing result
print("The Kth column of matrix is : " + str(res))

# ---------------
# print kth column of matrix (with k chosen randomly)
import numpy as np
import random
# initialize list
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
n = len(test_list[1]) # number of columns
# printing original list
print("The original list is : " + str(test_list))
#initialize K random
K = random.randrange(n)
print(K)
# Get Kth Column of Matrix
# using numpy
res = np.array(test_list)[:,K]
# printing result
print("The Kth column of matrix is : " + str(res))

# -------------
# print kth row of matrix (with k chosen randomly)
import numpy as np
import random
# initialize list
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
n = len(test_list[0]) # number of columns
# printing original list
print("The original list is : " + str(test_list))
#initialize K random
K = random.randrange(n)
print(K)
# Get Kth Column of Matrix
# using numpy
res = np.array(test_list)[K,:]
# printing result
print("The Kth row of matrix is : " + str(res))








'''
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


y = [1, 4, 6, 8, 11]
for i in y:
    if i % 2 == 0:
        print(i)
        y.remove(i)
print(y)
'''

y = [1, 4, 6, 8, 11]
for i in y:
    if i % 2 == 0:
        print(i)
        y.remove(i)
print(y)
# -----------




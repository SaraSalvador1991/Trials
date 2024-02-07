# max of the entrances of a vector
v = [10,22,9,11,72,100,99, 150]
max = 0
for i in range(len(v)):
    if v[i]>max:
        max = v[i]
print(max)

# ----------
 # check of palindrom

word = "Sara"

word = word.lower()
rev_word = reversed(word)

if list(word) == list(rev_word):
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")


# ----------

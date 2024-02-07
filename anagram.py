# check if two words are anagram

word1 = "tea"
word2 = "eat"

# if there are capital letters, lets put both words in lowercase

str1 = word1.lower()
str2 = word2.lower()

# of course, if the two words are not the same length, they cannot be anagram: lets check this
if (len(str1)==len(str2)):
    # to check if anagram let us sort the string (put the letters in alphabetic order
    sort1 = sorted (str1)
    sort2 = sorted(str2)
    if (sort1==sort2):
        print(word1 + " and " + word2 + " are anagram")
    else:
        print(word1 + "and " + word2 + "are not anagram")

else:
    print(word1 + " and " + word2 + " are not anagram")




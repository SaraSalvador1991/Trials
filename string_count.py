#s = 'armasuisse'
#c = s.count('a')
#print(c)

#file = open("README.md", "r")
#data = file.read().replace(" ", "")

#num = len(data)
#print(num)


file = open("/Users/sarasalvador/Desktop/prova.tex", "r")
data = file.read().replace(" ", "") #remove the spaces

num = len(data)
print(num)

# count of letter a
num_a = data.count('a')
print (num_a)

# count of letter ì

num_ì = data.count('ì')
print (num_ì)

# ------------- #

file = open("/Users/sarasalvador/Desktop/CV/prova_S.pdf", "r")
data = file.read().replace(" ", "") #remove the spaces

num = len(data)
print(num)


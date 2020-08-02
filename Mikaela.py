handle = open("GettysburgAddress.txt")
lame = open("GettysburgAddress.txt")

leng = len(handle.read())

all_freq = {} 

for i in (lame.read()): 
	if i in all_freq: 
		all_freq[i] += 1
	else: 
		all_freq[i] = 1

# printing result 
# print ("Count of all characters in GeeksforGeeks is :\n" + str(all_freq)) 

for letter in sorted(all_freq):
    print(letter, ':', all_freq[letter], ':', "{:.2f}".format((all_freq[letter] / leng) * 100), '%')



voule = ["A", "E", "I", "O", "U"]
for j in voule:
    print("{:.2f}".format((all_freq[j] / leng) * 100))


# print (voules & all_freq)

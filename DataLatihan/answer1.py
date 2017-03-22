data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
temp = readData(data1)
data = []
for i in temp:
	if i == "i" or i=="I": data.append("*")
	elif i =="You" or i=="The" or i == "And" : data.append("***")
	elif i =="you" or i=="the" or i == "and" : data.append("***")
	else : data.append(i)

data = " ".join(data)
print(data)
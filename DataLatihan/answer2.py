data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
temp1 = readData(data1)
temp2 = readData(data2)

data=[]
for i in temp1:
	if i in temp2:
		data.append(i)

newdata=[]
for j in data:
	if j not in newdata:
		newdata.append(j)

print(newdata)
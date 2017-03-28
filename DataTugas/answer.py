data = "DataSet.txt"

def readData(data):
	x = []
	with open(data) as data1 :
	    for line in data1 :
		    x = line.split()
	return x

answer = []
teks = readData(data)

for x in range(0,len(teks)-1):
	word = teks[x]
	if x == 0:
		word = word[0].upper()+word[1:]
	if word.isdigit()==True:
		word = word[::-1]
	if word[len(word)-1]==('.'):
		teks[x+1] = teks[x+1][0].upper() + teks[x+1][1:]
	answer.append(word)

word = teks[len(teks)-1]
answer.append(word)

answer = " ".join(answer)
print(answer)
import numpy as np
from sklearn import svm


file = open('training.txt','r').read()
l = ['.','!','?']
punc_char = np.array(l)
lgt = len(file)

num_of_pun = 0
lst = []
num_of_char = 5
lst = range(num_of_char,lgt-num_of_char)
for i in punc_char:
	num_of_pun = num_of_pun +  file.count(i)
varY = np.zeros((num_of_pun-1))
var1 = 54
c3 = 0
temp = 0 
lst = range(num_of_char,lgt-num_of_char)
X = np.zeros((num_of_pun-1,var1))


for c1 in  lst:
	if file[c1] in punc_char:
		cnt = 0
		c2 = c1
		
		# storing the left characters frequency
		
		while (cnt < num_of_char):
			
			c2 = c2 - 1
			
			if file[c2] >= 'A' and file[c2] <='Z':
				temp = ord(file[c2]) - ord('A')
				X[c3][temp] = X[c3][temp] + 1
				X[c3][26] =X[c3][26] + 1
				cnt =cnt + 1
			elif file[c2] >='a' and file[c2] <='z':
				temp = ord(file[c2]) - ord('a')
				X[c3][temp] = X[c3][temp] + 1
				cnt= cnt + 1
			if(cnt < num_of_char):
				break
		cnt = 0
		
		c2 = c1

		#storing the right characters frequency
		
		while (cnt < num_of_char):
			c2 = c2 + 1
			if file[c2] >= 'A' and file[c2] <='Z':
				temp = ord(file[c2])-ord('A')
				temp += 28
				X[c3][temp] +=1
				cnt = cnt + 1
				X[c3][27] = X[c3][27] + 1
				
			elif file[c2] >='a' and file[c2] <='z':
				if file[c2] == 's':
					if file[c2+1] != '>':
						temp = ord(file[c2])-ord('a')
						temp += 28
						cnt+=1
						X[c3][temp] = X[c3][temp] + 1
						
			if(cnt < num_of_char ):
				break
		if file[c1+1] == '<':
			varY[c3] = 1
		c3 +=1
		if c3 != num_of_pun-1:
			pass
		else:
			break
ratio = 0.91
Xtraining = X[:int(ratio*num_of_pun)]
Ytraining = varY[:int(ratio*num_of_pun)]
Ytest = varY[int(ratio*num_of_pun):]
Xtest = X[int(ratio*num_of_pun):]
classifier = svm.SVC()
classifier.fit(Xtraining,Ytraining)
prediction = classifier.predict(Xtest)
prediction = np.array(prediction)
Ytest = np.array(Ytest)
prediction = np.logical_and(prediction,Ytest)
leng = len(prediction)
num_of_tr = 0
num_of_fal = 0

for i in range(0,leng):
	if prediction[i] == True:
		num_of_tr += 1
	if prediction[i] == False:
		num_of_fal += 1
prcnt = (num_of_tr*100.0)/(num_of_fal + num_of_tr)
print ("The accuracy of the model is ",prcnt)
#print(sum(

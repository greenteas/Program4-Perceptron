from sklearn.linear_model import Perceptron
from charas import *

# USING SCIKIT LEARN 
# learning_rate = 0
# train_data = [eight,enter,man,destruction,to_assemble,perish]
# labels = ["eight", "enter", "man", "destruction", "to assemble", "perish"]

# for i in range(1,11):
# 	learning_rate = i/10

# 	print("learning rate:", learning_rate)
# 	p = Perceptron(eta0=learning_rate)
# 	p.fit(train_data, labels)

# 	a = p.predict(train_data)
# 	print(a)



import random
x = [eight,enter,man,destruction,to_assemble,perish]
t = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1]] #desired outputs
w = [] # weights
y = [] # gotten outputs
a = 1 # learning rate

threshold = 1

# append -1 to each data set
for data in x:
	data.append(-1)
	w.append(random.randint(0,9)/10)
	y.append([])

print(y)

w.append(threshold)
print(w)
i = 0

def all_equal(correct,outputs):
	all_in = True

	for a in correct:
		if a not in outputs:
			all_in = False
			break

	return all_in

while(not all_equal(t,y)):
	for j in range(0 ,len(x)):
		y[j] = 
		if not bool(set(y[j]).intersection(t[j])):
			# if output is not the desired output, update weights
			for i1 in range(len(w)):
				w[i1] = w[i1] + a * (t[i1] − y[i1]) * x[i1],
from sklearn.linear_model import Perceptron
from charas import *

# ------------ USING SCIKIT LEARN  ------------
learning_rate = 0
train_data = [eight,enter,man,destruction,to_assemble,perish]
labels = ["eight", "enter", "man", "destruction", "to assemble", "perish"]

# for i in range(1,11):
# 	learning_rate = i/10

# 	print("learning rate:", learning_rate)
# 	p = Perceptron(eta0=learning_rate)
# 	p.fit(train_data, labels)

# 	a = p.predict(train_data)
# 	print(a)


# ------------ TRAINING A CUSTOM MADE PERCEPTRON --------------
from perceptron import *

x = [eight,enter,man,destruction,to_assemble,perish]
t_list = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
y = 0 
a = .1 
theta = 10
iterations = 5 
p_list = [0,0,0,0,0,0] #store list of perceptrons

# train perceptrons to recognize characters
for alpha in range(0,3):
	a = alpha/10
	print("\n-------- ALPHA", a, "--------")
	for i in range(len(x)):
		temp_p = Custom_perceptron(x,t_list[i],a,theta)
		temp_p.train(iterations)
		p_list[i] = temp_p

	for i in range(len(x)):
		print(labels[i], "perceptron")
		for j in range(len(x)):
			print("\ttesting",labels[j], ":", p_list[i].predict(x[j]))
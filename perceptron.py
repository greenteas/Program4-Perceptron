import random
import numpy as np
import copy

class Custom_perceptron:
	def __init__(self,x,t,a,theta):
		self.x = copy.deepcopy(x) #input patterns
		self.t = t[:] #desired outputs
		self.a = a #learning rate
		self.theta = theta
		self.y = 0 # gotten output
		self.w = [] # weights

		for i in range(len(self.x[0])):
			self.w.append(random.randint(0,9)/10) #random starting weights
		self.w.append(theta)

		# append -1 to each data set
		for data in self.x:
			data.append(-1)

	def set_a(self,a):
		self.a = a

	def set_theta(self,theta):
		self.theta = theta

	def get_weights(self):
		return self.w

	def train(self, iterations):
		"""Train the perceptron, running iterations amount of times """
		for n in range(iterations):
			for j in range(0 ,len(self.x)): #for each input x
				if np.dot(self.x[j],self.w) > 0:
					# find dot product of each input see if there is a fire
					self.y = 1
				else:
					self.y = 0

				if self.y != self.t[j]:
					# if output is not the desired output, update weights
					for i1 in range(len(self.w)):
						self.w[i1] = self.w[i1] + self.a * (self.t[j] - self.y) * self.x[j][i1]

	def predict(self, data):
		"""Make a prediction about an input data"""
		temp = data[:]
		temp.append(-1) #augment data

		return np.dot(temp,self.w) > 0

	def all_equal():
		"""Checks if the weights work for all inputs and outputs."""
		all_in = True

		for j in range(0 ,len(x)): #for each input x
			if np.dot(x[j],w) != t[j]: #not equal to desired output
				all_in = False
				break

		return all_in
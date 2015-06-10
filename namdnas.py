import numpy
import math
import random
from matplotlib import pyplot as plt

def load_into_file(path):
	File = open(path, 'r')
	lines = File.readlines()
	# header = [title for title in lines[0].split(',')]
	# del lines[0]
	data = []
	for line in lines:
		row = []
		for element in line.split(' '):
			row.append(element)
		data.append(row)
	return data

def principal_component_analysis(data, tol):
	eig_val, eig_vec = numpy.linalg.eig(numpy.cov(data.T))
	eig_sum = 0
	for iter in range(len(eig_val)):
		eig_sum = eig_sum + eig_val[iter]
		if(eig_sum/sum(eig_val)>tol):
			break
	return eig_val[0:iter+1], eig_vec[0:iter+1]

def sequence(n):
	temp = 0
	seq = []
	seq.append(temp)
	for i in range(n):
		seq.append((seq[i]*seq[i] + 45)%1000000007)
	return seq

if __name__ == '__main__':
	path = "/home/jarvis/Documents/Sandman/seaco_updated_data.txt"
	data = load_into_file(path)
	name = raw_input("Enter your name>>>")
	print(name)
	data = numpy.matrix(data)
	pc_var, pc_vec = principal_component_analysis(data, tol=0.99)
	plt.plot(range(30))
	plt.show()
	
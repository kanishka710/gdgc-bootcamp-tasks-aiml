# Matrix times Vector
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c=[]
	if a is None or len(a[0]) != len(b):
		return -1
	for i in a:
		pdt=0
		for j in range(len(b)):
			pdt+= i[j]*b[j]
		c.append(pdt)
	return c
# Transpose of a Matrix
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b=[]
	for i in range(len(a[0])):
		for j in range(len(a)):
			b.append(a[j][i])
	return b
# Reshape Matrix
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if new_shape[0]*new_shape[1]!=len(a)*len(a[0]):
		return None
	mat=[]
	for i in a:
		for j in i:
			mat.append(j)	
	reshaped_matrix=[]
	s=0
	for i in range(new_shape[0]):
		ele=mat[s:s+new_shape[1]]
		reshaped_matrix.append(ele)
		s+=new_shape[1]
		# or
		# using numpy's reshape function
		x=np.reshape(a,new_shape)
	reshaped_matrix=x.tolist()
	return reshaped_matrix
# Calculate Mean by Row or Column
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode=='column':
		matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
	means=[]
	for i in matrix:
		means.append(sum(i)/len(i))
	return means
# Scalar Multiplication of a Matrix
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result=[[scalar*j for j in i]for i in matrix]
	return result
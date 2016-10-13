#! /usr/bin/python
from __future__ import division
import numpy
import random

'''
Grid object
'''
class Grid(object):
	
	def __init__(self, array):
		self.array = array
		self.x = (array == 'X').sum() 
		self.o = (array == 'O').sum()
		self.vacant = (array == ' ').sum() 
		self.length, self.width = array.shape
	

	'''
	Adjacent cells
	'''
	def adjacent(self, row,col):
		return Grid(numpy.array(self.array[(0 if row-1 < 0 else row-1):(self.length if row+2>self.length else row+2), range((0 if col-1 < 0 else col-1), (self.width if col+2>self.width else col+2))]))

	'''
	Removes agent
	'''
	def vacate(self, row, col): 
		self.array[row][col] = ' '	
		self.x = self.get_x()
		self.o = self.get_o()
		self.vacant = self.get_vacant()

	'''
	Places agent
	'''
	def place(self, row, col, agent): 
		if agent == ' ':
			return

		self.array[row][col] = agent	
		self.x = self.get_x()
		self.o = self.get_o()
		self.vacant = self.get_vacant()

	'''
	Computes the satisfaction of a specific cell
	'''
	def satisfaction(self, row, col):

		agent = self.array[row][col]
		sub = self.adjacent(row, col)
		if agent == ' ':
			return 1

		return round((getattr(sub, agent.lower())-1)/ (sub.x + sub.o - 1),4)

	'''
	Get specific agent
	'''
	def get_agent(self,x,y):
		return self.array[x][y]

	'''
	Get number of X agents
	'''
	def get_x(self):
		return (self.array == 'X').sum()

	'''
	Get number of O agents
	'''
	def get_o(self):
		return (self.array == 'O').sum()
 
 	'''
	Get number of vacant
	'''
 	def get_vacant(self):
		return (self.array == ' ').sum()
 
 	'''
 	Get coordinates of requested entity (X,O,' '). Default request is vacant
 	'''
 	def get_list(self, entity=' '):
 		lCoor = []
 		
 		if entity not in [' ', 'X','O']:
 			return lCoor

 		for i in range(self.length):
 			for j in range(self.width):
 				if self.array[i][j] == entity:
 					lCoor.append((i,j))

 		return lCoor
'''
Accepts a file parameter then converts the contents into a 2d array
'''
def loadgrid(file):
	list = []
	length = 0
	width = 0

	with open(file) as f:
		for row in f: 
			list.append([i for i in row.replace('\n','')])

	length, width = numpy.shape(list)

	return Grid(numpy.array(list))


'''
Computes for index of dissimilarity using 4 decimal places
'''
def dissimilarity(grid, row1, col1, row2, col2):
	sub = Grid(numpy.array(grid.array[row1:row2+1,range(col1,col2+1)].tolist()))
	index = round(0.5*abs(sub.x/grid.x - sub.o/grid.o), 4)
	return index



'''
Simplified
'''
def schelling(grid, t):
	if t < 0 or t > 1:
		return None 

	changed_flag = True

	while changed_flag:
		dissatisfied = []
		changed_flag = False
		for i in range(grid.length):
			for j in range(grid.width):
				if grid.satisfaction(i,j) < t:
					dissatisfied.append((i,j))

		for row,col in dissatisfied:
			grid.vacate(row,col)
			changed_flag = True
			
	return grid

'''
Segregates
'''
def schelling_segregate(grid,t):
	if t < 0 or t > 1:
		return None 

	changed_flag = True

	while changed_flag:
		dissatisfied = []
		changed_flag = False
		dissatisfied_agents = []
		for i in range(grid.length):
			for j in range(grid.width):
				if grid.satisfaction(i,j) < t:
					dissatisfied.append((i,j))
					dissatisfied_agents.append(grid.get_agent(i,j))

		vacant = grid.get_list()
		for row,col in dissatisfied:
			grid.vacate(row,col)
			vacant.append((row,col))
			changed_flag = True
			
		for agent in dissatisfied_agents:
			row,col = vacant.pop(random.randint(0,len(vacant)-1))
			grid.place(row,col, agent)

		print grid.array

	return grid	

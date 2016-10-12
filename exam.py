#! /usr/bin/python
from __future__ import division
import numpy

'''
Grid object. To store the number of x's and o's
'''
class Grid(object):
	
	def __init__(self, array):
		self.array = array
		self.x = (array == 'X').sum() 
		self.o = (array == 'O').sum() 
		self.length, self.width = array.shape
	

	def adjacent(self, row,col):
		return Grid(numpy.array(self.array[(0 if row-1 < 0 else row-1):(self.length if row+2>self.length else row+2), range((0 if col-1 < 0 else col-1), (self.width if col+2>self.width else col+2))]))

	def vacate(self, row, col): 
		self.array[row][col] = ' '	
 
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

'''
def schelling(grid, t):
	if t < 0 or t > 1:
		return None 

	
		

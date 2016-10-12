#! /usr/bin/python
import numpy

'''
Grid object. To store the number of x's and o's
'''
class Grid(object):
	
	def __init__(self, array):
		self.array = array
		self.x = (array == 'X').sum() 
		self.o = (array == 'O').sum() 

	

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

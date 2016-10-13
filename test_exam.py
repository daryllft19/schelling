#! /usr/bin/python

import unittest
from exam import *


class Test(unittest.TestCase):

	'''
	Tests if loadgrid with a file parameter will return Grid
	'''	
	def test_loadgrid(self):
		self.assertIsInstance(loadgrid('test.txt'), Grid)

	'''
	Dissimilarity should be a float
	'''	
	def test_dissimilarity(self):
		g = loadgrid('test.txt')
		row1 = random.randint(0,g.length-1)
		col1 = random.randint(0,g.width-1)
		row2 = random.randint(row1,g.length-1)
		col2 = random.randint(col1,g.width-1)

		self.assertIsInstance(dissimilarity(g, row1,col1,row2,col2), float) 
		self.assertEqual(dissimilarity(g,0,6, 3,9), 0.0209) 

	'''
	Schelling should return a grid after 100 rounds	
	'''	
	def test_schelling(self):
		g = loadgrid('test.txt')
		t = round(random.random(),2)
		print 'Testing schelling using threshold = ', t
		self.assertIsInstance(schelling(g,t, log=True, limit=100), Grid)

	'''
	Schelling segregate should return a grid after 100 rounds	
	'''	
	def test_schelling_segregate(self):
		g = loadgrid('test.txt')
		t = round(random.random(),2)
		self.assertIsInstance(schelling_segregate(g,t, log=True, limit=100), Grid)
		print 'Testing schelling segregate using threshold = ', t

if __name__ == '__main__':
	unittest.main()

#! /usr/bin/python
import numpy

def loadgrid(file):
	list = []
	length = 0
	width = 0

	with open(file) as f:
		for row in f: 
			list.append([i for i in row.replace('\n','')])

	length, width = numpy.shape(list)

	return numpy.array(list)


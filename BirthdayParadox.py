# BirthdayParadox.py
# Dennis
# 4/23/2019
# Random number generator between a and b
# Call until two elements match
# Use a hashtable
# 

# import numpy as np
import random
import collections
import matplotlib.pylab as plt

# In a set of n randomly chosen people
# Some pair of them will have the same birthday
# If n is greater than 366, it is 100% by PHP
# 99.9% chance occurs at 70 people
# 50% chance at 23
# Precondition: Probability of birthday on any given day is equal

birthdayDict = {}
iterationDistribution = {}
duplicateDay = 0
numIterations = 0
for j in range( 10000):
	for i in range( 366):
		numIterations += 1
		x = random.randint( 1, 366)
		# Check if x is in the dictionary
		if x in birthdayDict.keys():
			duplicateDay = x
			break
		# If x is not in the dictionary
		else:
			birthdayDict[x] = 1
	if duplicateDay in iterationDistribution.keys():
		iterationDistribution[duplicateDay] += 1
	else:
		iterationDistribution[duplicateDay] = 1
#print( "Number of random number generated", numIterations)
#print( "Date of duplication", duplicateDay)
#print( iterationDistribution)

lists = collections.OrderedDict( sorted( iterationDistribution.items(), key=lambda t: t[0]))
x, y = zip( *lists)
plt.plot( x, y)
plt.show()

























# Consider types of inputs
# Days in year 1, ..., 366
# Month/ Day
# Month/ Day/ Year


'''
def dateClean( string):
	if isinstance( string, int):
		return string
	if isisntance( string, float):
		return int( string)

	if isinstance( string, str):
		string = string.split('/')
		# Check if MM/DD or DD/MM
		if string.len() == 2:
			# Identify if MM/DD or DD/MM
			if string[0] > 12
			else if string[1] > 12
			else
		# Check if MM/DD/YY or DD/MM/YY
		if string.len() == 3:
			if string[0] > 12
			else if string[1] > 12
			else
	else:
		return
'''

import numpy
import csv
from numpy import *
# world_alcohol=numpy.genfromtxt("world_alcohol.csv",delimiter=",")
# print(type(world_alcohol))

vector=numpy.array([10,20,30])
matrix=numpy.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
])

# world_alcohol=numpy.genfromtxt("world_alcohol.csv",dtype="U75",skip_header=1,delimiter=",")


print vector.shape
print matrix.shape

print vector.dtype
print matrix.dtype

print(matrix[:,1]) # [10 25 40]
print(matrix[:,1:3])
# [[10 15]
# [25 30]
# [40 45]]

print (matrix[1:3:])
# [[20 25 30]
# [35 40 45]]

print (matrix[1:3,1]) # [25 40]

print(matrix[1:3,0:2])
# [[20 25]
#  [35 40]]


matrixA=random.rand(2, 2)
# creates numpy random matrix
# [[ 0.22421317  0.24935548]
#  [ 0.41561072  0.43697551]]


zeros()

# converting into python matrix from numpy matrix
pyMatrix = mat(matrixA)
inversePyMatrix = pyMatrix.I

print  "result of multiplication", pyMatrix*inversePyMatrix


print matrix.sum(axis=1) # all sum of row (axis=0) will give sum of columns
# mean(), max() etc. also can be used.

world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", skip_header=1, dtype="U75")
print(type(world_alcohol)) # <type 'numpy.ndarray'>
print world_alcohol
#showing row range

print ("Rows 1 to 3")
print world_alcohol[1:4,]

print ("Column 0 to 1")
print world_alcohol[:,0:2]

print ("First two row and first two column")
print world_alcohol[0:2,0:2]

#comparison in rows
# get boolean list column having year 1986
year_1986_col= "1986"==world_alcohol[:, 0]
print year_1986_col #[ True  True False ...,  True False  True]
# using above boolean list column get all rows having year 1986
print world_alcohol[year_1986_col,]
# [[u'1986' u'Western Pacific' u'Viet Nam' u'Wine' u'0']
# [u'1986' u'Americas' u'Uruguay' u'Other' u'0.5']
# [u'1986' u'Americas' u'Colombia' u'Beer' u'4.27']

country_switzerland= "Switzerland"==world_alcohol[:,2]

# get total alcohol consumption done in year 1986 and by switzerland
print world_alcohol[year_1986_col & country_switzerland, 4].astype(float).sum() # 14.07



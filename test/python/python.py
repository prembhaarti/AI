import time
import calendar

print "Python basic syntaxes" #basic print command

#standard datatypes : Numbers, nameing, List, Tuple, Dictionary
print("------------VARIABLE DECLARATION--------")
id, name = 5004, "Prem Bharti";
weight = 67.8

tripleQuoteString = """what are
you doing""" # using tripleQuote you can put your string in multiple line
# numbers in python are int,long(integer of large size),float,complex

print(id)
print(weight)

print (name)          # Prints complete nameing
print (name[0])       # Prints first character of the nameing -> P
print (name[1:4])     # Prints characters starting from 3rd to 5th -> em 
print (name[2:])      # Prints nameing starting from 3rd character -> em bharti
print (name * 2)      # Prints nameing two times -> Prem BhartiPrem Bharti

print (name + " TEST") # Prints concatenated namein -> Prem Bharti TEST

#play with datatype
print(type(weight)) 	# type returns the data type variable belongs to
print(str(weight))
print(int(weight))


# operators ( +, - , *, /, **)

print(2**3)	# ** works as exponent

# order execution of operators -> P,E,M,D,A,S -> parenthesis, exponential, multiply, division, addition, subtraction

#comparison :below returns true
# "prem" == "prem"
# 8.0 == 8.0
# ["love","bharti"] == ["love","bharti"]




# LIST -> can contain heterogeneous elements
print("----------------LIST---------------")
employeeDetail = [ id, name , weight, 'Senior Software Engineer']
tinylist = [123, 'john']

print (employeeDetail)          # Prints complete list
print (employeeDetail[0])       # Prints first element of the list
print (employeeDetail[-1])		# Prints first element from end of list
print (employeeDetail[1:3])     # Prints elements starting from 2nd till 3rd 
print (employeeDetail[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (employeeDetail + tinylist) # Prints concatenated lists

print([1,2,4]+[3,5])
del tinylist; # it will delete tinylist, using tinylist after this will show error
#print tinylist




#TUPLES ->  Tuples can be thought of as read-only lists. So, you need to set it's elements while defining
print("-----------------TUPLE------------")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

employeeDetail[2] = 70.0 # Valid syntax with list
#tuple[1] = 1000     # InValid syntax with tuple, will give error

#DICTIONARY : are kind of hash table type. They work like associative arrays
# Dictionaries have no concept of order among elements.
print("--------------DICTIONARY-----------")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

del tinydict['dept']
tinydict['addedKey']='addedValue'
print(tinydict);
#dict.clear() # will remove all entries in dictionary
#del dict # will delete dictionaries.

print("-------TYPE CONVERSION-------")

print(int("50"))
print(float("50.0"))
print(chr(5))

print("-----------------Operators------------------")
empIds=[001,002,003,004]
if(001 in empIds):
	print "001 is available in list"
elif(002 in empIds):
	print "002 is available in list"
else:
	print "001 is not available in list"
print(001 not in empIds)

num1=20
num2=20
if(num1 is num2):
	print("num1 is same as num2")
if(num1 is not num2):
	print("num1 is not same as num2")
if not(num1 is num2):
	print("num1 is not same as num2")

#if( id(num1) == id(num2) ):
#	print("num1 and num2 are same")
print("-----------LOOPS-----------")
count=0
while(count<9):
	print 'Count:',count
	count+=1
else:
	print "loop condition failed"
print "loop ended"

for empDetail in employeeDetail:
	print empDetail

for letter in 'Python':     # First Example
   print 'Current Letter :', letter

for i in range(1,5):
   print "number", i   

# Bubble sort in python
print("---------BUBBLE SORT-----------")
numList=[4,2,1,0,10]

for i in range(len(numList)-1,1,-1): # reverse range
	for j in range(0,i):
		if numList[j]>numList[i]:
			numList[i],numList[j]=numList[j],numList[i] # swapping done

for k in range(len(numList)):
 print numList[k]

print("--------TIME----------")
ticks = time.time();
print "Number of ticks since 12:00am, January 1, 1970:",ticks


localtime = time.localtime(time.time())
print "Local current time :", localtime

cal = calendar.month(2016, 12)
print "Here is the calendar:"
print cal

print("----------function-----------")

# All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter
# refers to within a function, the change also reflects back in the calling function

# declare function
def factorial(num):
	if (num>1) : return num*factorial(num-1)
	else : return 1
# call function
print(factorial(8))

# method with default parameter
def defaultParamMethod(param1, defaultParam="Love"):
	print param1," ",defaultParam

defaultParamMethod("Bharti")

# variable arguement method
def variableParamMethod(param1, *extraParams):
	print param1
	for extraParam in extraParams:
		print extraParam

variableParamMethod(1,2,3,4,5)

# using lambda for a method
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )

#list

countries = ["India","Pakistan","Australia","Sri lanka","Bangaladesh"]
print ("India" in countries)
print ("India" not in countries)
print (len(countries))
countries.append("New Zealand")




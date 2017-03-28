import sys

def factorial(num):
	if (num>1) : return num*factorial(num-1)
	else : return 1

#def fibonacci(num):
#	if(num>2) : return fibonacci(num-1)+fibonacci(num-2)
#	if(num==1||num==2): return 1


def swap(num1,num2):
	num1,num2=num2,num1

def largestContiguousSum(arr):
	resultSum=-sys.maxsize
	currentSum=0;	
	for i in range(0,len(arr)):
		currentSum+=arr[i]
		if(currentSum<0):
			currentSum=0
		elif(currentSum>resultSum):
			resultSum=currentSum
	
	return resultSum		

num=[1,2,3,4,-1,7,2]

print(largestContiguousSum(num))
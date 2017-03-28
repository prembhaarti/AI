class Employee:

	empCount=0;

	def __init__(self, id, name, designation):
		self.id = id
		self.name = name
		self.designation = designation
		Employee.empCount+= 1

	def getAverageSalaryByDesig(self, designation):
		if(self.designation=="se"):
			return "9lpa"
		elif(self.designation=="sse"):
			return "10lpa"
		else:
			return "11lpa"

	def toString(self):
		print "id :%d, name:%s, designation:%s" %(self.id, self.name, self.designation)

emp1= Employee(1, "Prem Bharti", "se")
# print(getattr(emp1,"id"))
# setattr(emp1,"id",5004)
# print(getattr(emp1,"name"))
# print(getattr(emp1,"designation"))
print emp1.getAverageSalaryByDesig("se")
print Employee.empCount;
emp1.toString()

emp2= Employee(2,"Naveen","sse")
emp2.toString()
print Employee.empCount
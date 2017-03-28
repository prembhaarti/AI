class Employee():

    def getDesigNation(self):
        return "Yatra Employee"

    def getCompany(self):
        return "Yatra"

class SSE(Employee):

    def getDesigNation(self):
        return "SSE"


sse = SSE()
print sse.getCompany()
print sse.getDesigNation()

emp = Employee()
print emp.getCompany()
print emp.getDesigNation()
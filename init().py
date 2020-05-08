class hello:
	leaves = 8
	
	def printdetails(self):
		print("Name is :-",self.name,",","Salary is :-",self.salary)

parth = hello()
parth.name = "Parth Patel"
parth.salary = 50000
parth.printdetails()

class Employee:
	def __init__(self,aname,asalary):
		self.name = aname
		self.salary = asalary
	def printdetails1(self):
		print("Name is :-",self.name,",","Salary is :-",self.salary)
	
parth1 = Employee("Parth",50000)
parth1.printdetails1()

deposit  = int(input("Enter the deposit Value:-"))
parth1.salary = parth1.salary + deposit
parth1.printdetails1()

	

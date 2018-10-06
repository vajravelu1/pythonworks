#!/play/p1/bin/python

class Employee:
	def __init__(self,name,age,place):
		self.name=name
		self.age=age
		self.place=place


	def get_emp_details(self):
		return f'\t\t\t employee name    : {self.name} \n \
			 age		  : {self.age} \n \
			 place		  : {self.place}'
	


class Techie(Employee):
	def __init__(self,name,age,place,tech_skill):
		Employee.__init__(self,name,age,place)
		self.tech_skill=tech_skill

	def fn1(func):
		def wrapper(*args,**kwargs):
			print(Employee.get_emp_details(self))
			res1=func(*args,**kwargs)
			return res1
		
	@fn1
	def get_emp_details(self):
		return	f'\t\t\t technology	  : {self.tech_skill}'


e1=Employee('Vajravelu',30,'Bangalore')
e2=Techie('Raghuram',40,'Tumkur','java')

print(e1.get_emp_details())
print()
print(e2.get_emp_details())

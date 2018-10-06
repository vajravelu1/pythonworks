#!/play/p1/bin/python


class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last

	def get_details(self):
		print(self.first)
		print(self.last)
		print(self.email)

	@property
	def email(self):
		print(f'{self.first}.{self.last}@company.com')
	
	@email.setter
	def email(self,email_str):
		first,last=email_str.split('@')[0].split('.')
		self.first=first
		self.last=last

	
	@email.deleter
	def email(self):
		self.first='blah'
		self.last='errr'
	

e1=Employee('Vajravelu','Mani')
e1.email='abc.xyz@company.com'

e1.get_details()

del e1.email
e1.get_details()

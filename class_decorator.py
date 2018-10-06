#!/play/p1/bin/python

class Call_count:
	def __init__(self,func):
		self.func=func
		self.count=0

	def __call__(self,*args,**kwargs):
		self.count+=1
		return self.func(*args,**kwargs)


@Call_count
def hello(name):
	print(name)

hello('vajravelu')
hello('dfd')
hello('dsadsadsa')

print(f'{hello.count}')

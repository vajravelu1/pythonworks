#!/play/p1/bin/python

import time

def time_it(func):
 def wrapper(*args,**kwargs):
  start=time.time()
  result=func(*args,**kwargs)
  end=time.time()
  print(f'the time taken to execute {func.__name__} is {(end-start)*1000} milli seconds')
  return result
 return wrapper

@time_it
def squarify(x):
 result=[]
 for i in x:
  result.append(i*i)
 return result

@time_it
def cubify(x):
 result=[]
 for i in x:
  result.append(i*i*i)
 return result


array1=range(1,10000)
sq1=squarify(array1)
cb1=cubify(array1)

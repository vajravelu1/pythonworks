def dec1(a):
 def val1(func):
  def wrap1(*args,**kwargs):
   if len(*args) == a:
    print('success')
   else:
    print('params of base fn are not of expected length')
    print(f'given length: {len(*args)}')
   func(*args,**kwargs)
  return wrap1
 return val1


@dec1(5)
def fn1(mess1):
 ''' function 1 prints message from base function '''
 print(mess1)
 return


#!/play/p1/bin/python

class Vehicle:
 wheel=0

 def __init__(self):
  pass
 
 @classmethod
 def bike(cls):
  print(f'wheel count previously was : {cls.wheel}')
  cls.wheel=2
  print(f'Bike has : {cls.wheel} wheels')

 @classmethod
 def car(cls):
  print(f'wheel count previously was : {cls.wheel}')
  cls.wheel=4
  print(f'Car has : {cls.wheel} wheels')


ins1=Vehicle()
Vehicle.bike()
Vehicle.car()
ins1.bike()
ins1.bike()
ins1.car()
ins1.bike()

#!/play/p1/bin/python

from contextlib import closing

class FridgeRaider:
	def open_door(self):
		print('opening fridge door')

	def get_food(self,food):
		print(f'finding {food}')
		if food == 'butter paneer':
			raise RuntimeError('thats a unhealthy food')
		print(f'taking {food}')
	
	def close(self):
		print('closing fridge door')

def get_food(x):
	with closing(FridgeRaider()) as e:
		e.open_door()
		e.get_food(x)

		
		
####sample edit###

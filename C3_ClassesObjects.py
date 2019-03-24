#class is a blueprint for a data or behaviour

class Vehicle:
	def __init__(self, color, seats, fuel, horse_power):
		self._color=color
		self._seats=seats
		self._fuel=fuel
		self._horse_power=horse_power
		
		print()
	
	pass
car=Vehicle('black', 4, 'gas', 170)
print(car._color,car._seats,car._fuel)


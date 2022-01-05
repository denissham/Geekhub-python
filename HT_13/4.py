# Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» 
# та приймав кольор фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.

class Figure(object):
	color = "white"

	def __init__(self, new_color):
		Figure.color = new_color
		return Figure.color

class Oval(Figure):
	def __init__(self, oval_length, oval_width, new_color):
		self.length = oval_length
		self.width = oval_width
		Figure.__init__(self, new_color)


class Square(Figure):
	def __init__(self, square_length, new_color):
		self.length = square_length
		Figure.__init__(self, new_color)



oval = Oval(13,15,"blue")
print(oval.color)
print(oval.length)
square = Square(12, "red")
print(square.color)
print(square.length)
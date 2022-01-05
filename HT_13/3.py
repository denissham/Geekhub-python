# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і метод для зміни кольору фігури, 
# а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

class Figure(object):
	color = "white"

	def change_color(self, new_color):
		Figure.color = new_color
		return Figure.color

class Oval(Figure):
	def __init__(self, length, width):
			self.__length = length
			self.__width = width


class Square(Figure):
	def __init__(self, length_a):
			self.__length_a = length_a

oval = Oval(13,15)
print(oval.color)
square = Square(12)
print(square.color)
			



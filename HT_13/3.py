# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і метод для зміни кольору фігури, 
# а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

class Figure(object):
	color = "white"

	def change_color(self, new_color):
		self.color = new_color
		

class Oval(Figure):
	def __init__(self, length, width):
			self.length = length
			self.width = width


class Square(Figure):
	def __init__(self, length_a):
			self.length_a = length_a

oval = Oval(13,15)
oval.change_color("red")
print(oval.color)
square = Square(12)
print(square.color)


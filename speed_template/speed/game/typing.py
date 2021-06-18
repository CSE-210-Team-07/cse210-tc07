
from game.actor import Actor
from game.point import Point


class Typing(Actor):

	def __init__(self):
		"""The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.

		Args:
			self (Score): an instance of Score.
		"""
		super().__init__()
		self._letters = ""
		position = Point(0, 20)
		self.set_position(position)
		self.set_text(f"Buffer: {self._letters}")

	def add_letter(self, letter):
		"""Adds the given points to the running total and updates the text.

		Args:
			self (Score): An instance of Score.
			points (integer): The points to add.
		"""
		self._letters += letter
		self.set_text(f"Buffer: {self._letters}")

	def get_letters(self):
		ret = self._letters
		self._letters = ""
		self.set_text(f"Buffer: ")
		return ret



					

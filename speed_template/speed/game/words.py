from game import constants
from game.actor import Actor
from game.point import Point
import random 
from game.constants import LIBRARY 

class Words:


    def __init__(self):
        self._words = []
        self._prepare_word() 

    def get_all(self):

        return self._words

    def rand_word(self):
        randword = random.choice(LIBRARY)
        return randword 

    def move_word(self):
        count = len(self._words) - 1
        for n in range(count, -1, -1):
            word = self._words[n]
            word.move_next()

    def _prepare_word(self):
        position = Point(random.randint(0,60), random.randint(0,20)) 
        velocity = Point(0,1) 
        word = Actor()
        word.set_text(self.rand_word())
        word.set_position(position)
        word.set_velocity(velocity)   
        self._words.append(word)
	
	def _check_word(self, word):
		buff = []
		for i in self._words:
			if i != word:
				buff.append(i)
		self._words = buff
				
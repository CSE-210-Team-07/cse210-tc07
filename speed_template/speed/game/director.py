from game.input_service import InputService


class Director:
	def __init__(self, input_service, output_service):
		self.input_service = input_service
		self.output_service = output_service
		# general con - mens, black guy, lastname is corbitt
		return
	
	def start_game(self):

		print(self.input_service.get_letter() + "-")
		return
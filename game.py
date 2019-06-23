#!/usr/bin/python3

from world import World

class Game:
	def __init__(self):
		self.world = World(mapsize=10)
		self.clock = 0
		self.running = False
		self.ticks = 0

	def entrypoint(self):
		self.world.start()

	def tick(self):
		self.ticks += 1
		self.entrypoint()
		self.running = not self.ticks >= 1

	def start(self):
		while True:
			self.tick()
			if not self.running:
				break

if __name__ == '__main__':
	game = Game()
	game.start()

#!/usr/bin/python3

import time

from event import Event
from world import World

class Game(Event):
	def __init__(self):
		self.world = World(mapsize=10)
		self.clock = 0
		self.ticks = 0

	def run(self):
		self.entrypoint()
		while True: # self.ticks < 50:
			self.tick()
			time.sleep(1)
		self.shutdown()

	def shutdown(self):
		pass

	def tick(self):
		self.ticks += 1
		self.world.tick()
		print(self.world.render())

	def entrypoint(self):
		self.world.start()

if __name__ == '__main__':
	game = Game()
	game.run()

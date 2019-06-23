#!/usr/bin/python3

from player import Player
from map import Map

class World:
	def __init__(self, mapsize):
		self.map = Map(mapsize)
		self.actors = []

	def start(self):
		self.load_actors()
		print(self.map.render())

	def load_actors(self):
		p = Player("ThePlayer", 9001)
		self.map.set(self.map.size/2 - 1, self.map.size/2 - 1, p)
		self.actors.append(p)

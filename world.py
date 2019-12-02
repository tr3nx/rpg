#!/usr/bin/python3

from event import Event
from player import Player
from map import Map

class World(Event):
	def __init__(self, mapsize):
		self.map = Map(mapsize)
		self.shadow = self.map
		self.actors = []

	def start(self):
		self.load_actors()

	def render(self):
		return self.map.render()

	def tick(self):
		for actor in self.actors:
			actor.update()

	def load_actors(self):
		p = Player("ThePlayer")
		self.map.set(p.pos, p)
		self.actors.append(p)

#!/usr/bin/python3

from actor import Actor

class Map:
	def __init__(self, size):
		self.size = size
		self.map = {}
		self.clear_entire()

	def set(self, x, y, entity):
		self.map[(x, y)] = entity
		return self

	def get(self, x, y):
		return self.map[y][x]

	def check(self, x, y):
		return self.get(x, y) > 0

	def clear(self, x, y):
		self.set(x, y, 0)
		return self

	def clear_entire(self):
		for x in range(self.size):
			for y in range(self.size):
				self.clear(x, y)

	def render(self):
		out = ""
		for x in range(self.size):
			for y in range(self.size):
				entity = self.map[(x, y)]
				if isinstance(entity, Actor):
					out += self.map[(x, y)].render()
				else:
					out += '.'
				out += " "
			out += "\n"
		return out

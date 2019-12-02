#!/usr/bin/python3

from actor import Actor

class Map:
	def __init__(self, size):
		self.size = size
		self.map = {}
		self.clear_entire()

	def set(self, pos, entity):
		self.map[pos] = entity
		return self

	def get(self, pos):
		return self.map[pos[0]][pos[1]]

	def check(self, pos):
		return self.get(pos) > 0

	def clear(self, pos):
		self.set(pos, 0)
		return self

	def clear_entire(self):
		for x in range(self.size):
			for y in range(self.size):
				self.clear((x, y))

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

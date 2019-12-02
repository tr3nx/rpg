#!/usr/bin/python3

from event import Event

class Actor(Event):
	def __init__(self, name="", pos=(0, 0), health=0, model="", isplayer=False, active=False, hidden=False, inventory=[], attributes=[], scripts=[]):
		self.name = name
		self.pos = pos
		self.health = health
		self.active = active
		self.hidden = hidden
		self.model = model
		self.isPlayer = isplayer
		self.attributes = attributes
		self.scripts = scripts
		self.inventory = inventory

	def update(self):
		print ("actor update: ", self.name)
		for script in self.scripts:
			getattr(self, script.__name__)()

	def render(self):
		return self.model

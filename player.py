#!/usr/bin/python3

from event import Event
from actor import Actor
from inventory import Inventory
from quests import QuestLog

class Player(Actor):
	def __init__(self, name, health=100):
		super(Player, self).__init__(name=name, pos=(2, 7), model="@", health=100, isplayer=True, inventory=Inventory())
		self.questlog = QuestLog()
		self.scripts = [self.movearound]

	def movearound(self):
		self.pos = (6, 6)

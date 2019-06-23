#!/usr/bin/python3

from actor import Actor
from inventory import Inventory
from quests import QuestLog

class Player(Actor):
	def __init__(self, name, health=100):
		super(Player, self).__init__(name)
		self.health = health
		self.inventory = Inventory()
		self.questlog = QuestLog()

	def render(self):
		return '@'

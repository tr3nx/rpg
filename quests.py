#!/usr/bin/python3

from item import Item

class QuestLog:
	def __init__(self):
		self.quests = []

class Quest:
	def __init__(self, name, objectives, rewards):
		self.name = name
		self.objectives = objectives
		self.rewards = rewards

	def is_completed(self):
		return False

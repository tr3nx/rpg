#!/usr/bin/python3

class Item:
	def __init__(self, name, slot, model):
		self.name = name
		self.slot = slot
		self.model = model

class Gold(Item):
	def __init__(self, amount=1):
		self.amount = amount

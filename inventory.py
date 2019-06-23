#!/usr/bin/python3

from item import Item

class Inventory:
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def remove(self, item):
		self.items.remove(item)

	def has(self, item):
		return item in self.items

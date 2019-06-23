#!/usr/bin/python3

from item import Item
from player import Player
from world import World
from scripted import Script

class UI:
	def __init__(self):
		self.out = ""

	def write(self, message):
		self.out += message

	def render(self):
		out = self.out
		self.clear()
		return out

	def clear(self):
		self.out = ""

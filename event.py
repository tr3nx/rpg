#!/usr/bin/python3

class Event:
	def __init__(self):
		self.events = ()
		self.queue = ()

	def emit(self, name, data):
		self.queue.append({ "name": name, "data": data });

	def handler(self, name, fn):
		self.events.append({ "name": name, "fn": fn })

	def process(self):
		for e in self.queue:
			print(e.name)

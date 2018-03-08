#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
It is main mehod
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
import requests
import os
import re
import argparse

__author__ = "xuanchen yao"
__copyright__ = "xuanchen yao"
__license__ = "mit"

_logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Add command --input')
parser.add_argument('--input', help='The program will count the rest of bright lights after tests. Using command "solve_led --input fileAddress" ')
args = parser.parse_args()



from numpy import *
class ledController(object):
	"""docstring for ledController"""
	lights = None
	def __init__(self, file):
		self.file = file
		self.lights = array([[False]*0 for _ in range(0)])
		self.size = 0

	def parseFile(self):
		instructions = []
		if self.file.startswith('http'):
			try:
				content = requests.get(self.file).text
				self.size = int('\n'.join(content.split('\n')[:1]))
				instructions = ('\n'.join(content.split('\n')[1:])).split('\n')
				return self.size, instructions
			except urllib.error.HTTPError:
				print("The URL is error.")
		else:
   			if os.path.exists(self.file):
   				with open(self.file, 'r') as f:
   					self.size = int(f.readline())
   					for line in f.readlines():
   						instructions.append(line)
   				return self.size, instructions
   			else:
   				return "File doesn't exist."

	def initializeLights(self):
		self.lights = array([[False]*self.size for _ in range(self.size)])

	def command(self, instructions):
		command = re.compile(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
		for i in range(len(instructions)):
			b = command.match(instructions[i])
			if b:
				x1, y1, x2, y2 = int(b.group(2)),int(b.group(3)),int(b.group(4)),int(b.group(5))
				x1, x2 = max(min(x1, x2), 0), min(max(x1, x2), self.size-1)
				y1, y2 = max(min(y1, y2), 0), min(max(y1, y2), self.size-1)
				if ((x2>=0) and (y2>=0)):
					if b.group(1) == "turn on":
						self.lights[x1:x2+1, y1:y2+1]=True
					elif b.group(1) == "turn off":
						self.lights[x1:x2+1, y1:y2+1]=False
					else:
						#map(switch,self.lights[x1:x2][y1:y2])
						self.lights[x1:x2+1, y1:y2+1]=(self.lights[x1:x2+1, y1:y2+1]*-1+True).astype(bool)
		print("The left number of the rest of bright lights is",count_nonzero(self.lights))
		return count_nonzero(self.lights)

def main():
	file = args.input
	test_lights = ledController(file)
	size, instrucions = test_lights.parseFile()
	test_lights.initializeLights()
	return(test_lights.command(instrucions))


if __name__ == '__main__':
	main()


   	

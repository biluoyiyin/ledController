#!/usr/bin/env python
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

__author__ = "xuanchen yao"
__copyright__ = "xuanchen yao"
__license__ = "mit"

_logger = logging.getLogger(__name__)

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
			content = requests.get(self.file).text
			self.size = int('\n'.join(content.split('\n')[:1]))
			instructions = ('\n'.join(content.split('\n')[1:])).split('\n')
			return self.size, instructions
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
				x1, x2 = min(x1, x2), max(x1, x2)
				y1, y2 = min(y1, y2), max(y1, y2)
				if x2 < self.size and y2 < self.size :
					if b.group(1) == "turn on":
						self.lights[x1:x2+1, y1:y2+1]=True
					elif b.group(1) == "turn off":
						self.lights[x1:x2+1, y1:y2+1]=False
					else:
						#map(switch,self.lights[x1:x2][y1:y2])
						self.lights[x1:x2, y1:y2]=(self.lights[x1:x2, y1:y2]*-1+True).astype(bool)
		return count_nonzero(self.lights)

def main(file):
	test_lights = ledController(file)
	size, instrucions = test_lights.parseFile()
	test_lights.initializeLights()
	return(test_lights.command(instrucions))






   	

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

	def parseFile(self):
		N, instructions = None, []
		if self.file.startswith('http'):
			content = requests.get(self.file).text
			N = int('\n'.join(content.split('\n')[:1]))
			instructions = ('\n'.join(content.split('\n')[1:])).split('\n')
			return N, instructions
		else:
   			if os.path.exists(self.file):
   				with open(self.file, 'r') as f:
   					N = int(f.readline())
   					for line in f.readlines():
   						instructions.append(line)
   				return N, instructions
   			else:
   				return "File doesn't exist."

	def initializeLights(self, size):
		self.lights = array([[False]*size for _ in range(size)])



   	

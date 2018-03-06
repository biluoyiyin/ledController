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
	def __init__(self, size):
		self.lights = array([[False]*size for _ in range(size)])

	def parseFile(self, file):
		if file.startswith('http'):
			return "web"
		else:
   			if os.path.exists(file):
   				return True
   			else:
   				return False


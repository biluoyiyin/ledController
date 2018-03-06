#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
It is main mehod
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging

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

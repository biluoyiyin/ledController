#!/usr/bin/env python
# -*- coding: utf-8 -*-

    
__author__ = "xuanchen yao"
__copyright__ = "xuanchen yao"
__license__ = "mit"

import pytest
from ledController.main import ledController

 
class Test_main(object):
	"""docstring for Test_main"""
	def test_ledController(self):
		array = ledController(999)
		assert array.lights.shape == (999, 999)

	def test_fileExistence(self):
		array = ledController(9)
		file = "./data/test_data.txt"
		assert array.parseFile(file)==True
    	

		
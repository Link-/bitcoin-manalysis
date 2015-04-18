import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))

import unittest
import json_obj as jobj

class JSONobjTest(unittest.TestCase):

	# Setup the JSONobject
	def setUp(self):
		# A valid json file
		# needs to be chosen for this
		file_path = '/Users/bassemd/Projects/bitcoin-manalysis/json_to_csv/_raw_data/hot-bitcoin1427836487.05.json'
		self.tobj = jobj.JSONobj(file_path)

	def tearDown(self):
		pass

	# Testing whether the object
	# has the proper arguments
	def test_sufficient_args(self):
		# Chose a valid json file
		# path for this test
		file_path = '/Users/bassemd/Projects/bitcoin-manalysis/json_to_csv/_raw_data/hot-bitcoin1427836487.05.json'
		jobj.JSONobj(file_path)

	# Test the getter method
	# whether it returns a null
	# value (which should never
	# be the case)
	def test_get_file_path(self):
		self.assertNotEquals(self.tobj.get_file_path(), '')

	# Test whether validate_file()
	# module raises a file does not
	# exist exception (os.error)
	def test_validate_file_exists(self):
		self.assertRaises(Exception, self.tobj.validate_file())

	# Test whether validate_file()
	# module raises a file does not
	# exist exception (os.error)
	# for the get_size() module
	def test_validate_file_size(self):
		self.assertRaises(Exception, self.tobj.validate_file())

	# Test whether validate_file()
	# returns true when everything is
	# in order (test is done with
	# a pre-existing file)
	def test_validate_file_true(self):
		# Set the file_path to this file
		self.tobj.file_path = __file__
		# Check if it's true
		self.assertTrue(self.tobj.validate_file())

	# Test whether a wrong filename
	# that does not exist will raise
	# the proper exception
	def test_validate_file_false(self):
		# Set the file_path variable to a known
		# non existent file
		self.tobj.file_path = __file__ + 'something'
		# Check if the method raises an exception
		self.assertRaises(Exception, lambda: self.tobj.validate_file())

	# Test whether the set json file
	# loads and can be data filled into
	# an object
	def test_read_json_file(self):
		# Quick test the file size
		# it should be greater than 0
		self.assertGreater(self.tobj.get_file_size(), 0, 'TRJF: File is not empty!')
		# if the JSON file is opened
		# and read properly the method
		# should return true since the object
		# is not empty
		# NOTE: we should know for a fact
		# that the sample JSON file
		# is NOT EMPTY
		self.assertTrue(self.tobj.read_json())

if __name__ == '__main__':
	unittest.main()
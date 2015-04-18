#
# JSON Object
#

import os
import json

class JSONobj(object):

	def __init__(self, file_path):
		# Raise an exception
		# if the file_path argument
		# is not passed
		if not file_path:
			raise Exception("file_path is not defined")
		# Set the local file_path
		self.file_path = file_path
		# Validate file exists and
		# is not empty
		self.validate_file()

	# Validate whether:
	# 1. File exists
	# 2. File size > 0 (not empty)
	# Raise an exception otherwise
	def validate_file(self):
		# Validate exist
		if not os.path.exists(self.file_path):
			raise Exception("File does not exist")
		# Validate size
		if os.path.getsize(self.file_path) == 0:
			raise Exception("File is empty")
		# Return True otherwise
		return True

	# Getter method that
	# returns the actual file
	# size
	def get_file_size(self):
		return os.path.getsize(self.file_path)

	# Getter method that returns
	# the JSON file path
	def get_file_path(self):
		return self.file_path

	# Set the output directory
	# for the converted
	# output CSV file
	def set_output_dir(self, out_path):
		self.out_path = out_path
		# If parameter is empty
		# raise an exception
		if not self.out_path:
			raise Exception("Output directory cannot be empty!")
		# First check if directory
		# exists
		if not os.path.exists(self.out_path):
			# if not, create it
			os.makedirs(self.out_path)

	# Method that reads the content
	# set JSON file and stores
	# it in an object
	def read_json(self):
		with open(self.file_path) as json_file:
			# Return the JSON object
			return json.load(json_file)

	# Main converter from
	# JSON object to CSV
	def convert(self):
		return ''
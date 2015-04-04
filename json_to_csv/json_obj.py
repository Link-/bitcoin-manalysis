#
# JSON Object
#

import os

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
		else:
			return True



	# Getter method that returns
	# the JSON file path
	def get_file_path(self):
		return self.file_path
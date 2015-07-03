#!/usr/bin/python
# 
# Python JSON to CSV translator
# 
# @version: 0.1.0
#
# run: 
# $ 
#

import json_obj as jobj
from pprint import pprint
import jsontree

global_dictionary = {}

def main():
	local_obj = jobj.JSONobj('/Users/bassemd/Projects/bitcoin-manalysis/json_to_csv/_raw_data/hot-bitcoin1427836487.05.json')
	# local_obj = jobj.JSONobj('/Users/bassemd/Projects/bitcoin-manalysis/json_to_csv/_raw_data/1itemonly.json')
	print local_obj.get_file_path()
	json_tree = local_obj.read_json()

	walk(json_tree)

	pprint(global_dictionary)

def walk(node):
	# Check if the node is a dictionary
	# or a list (based on the JSON
	# translation table
	if isinstance(node, dict):
		# Loop through the dictionary
		for key, value in node.items():
			# If the item is a dictionary or
			# a list then recurse
			if isinstance(value, dict) or \
			   isinstance(value, list):
				walk(value)
			# If not, then it's a leaf
			# print the value
			else:
				# print key, value
				# Append into the dictionary the value
				# if it's not empty and NA if empty
				# make sure that the key already exists
				# if not add a new key
				global_dictionary.setdefault(key, []).append(value if bool(value) == True else 'None')
	# If the node is a list
	# loop through the list
	elif isinstance(node, list):
		for item in node:
			# if the item is a dictionary or
			# a list then recruse
			if isinstance(item, dict) or \
			   isinstance(item, list):
				walk(item)
			# If not, the it's a leaf
			# print the value
			else:
				# print item.key, item.value
				# Append into the dictionary the value
				# if it's not empty and NA if empty
				# make sure that the key already exists
				# if not add a new key
				global_dictionary.setdefault(item.key, []).append(item.value if bool(item.value) == True else 'None')
	# If it's not all the above
	# then it's a leaf, print
	# the value
	else:
		# print node.key, node.value
		# Append into the dictionary the value
		# if it's not empty and NA if empty
		# make sure that the key already exists
		# if not add a new key
		global_dictionary.setdefault(node.key, []).append(node.value if bool(node.value) == True else 'None')

if __name__ == "__main__":
	main()
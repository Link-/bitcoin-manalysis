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

def main():
	local_obj = jobj.JSONobj('/Users/bassemd/Projects/bitcoin-manalysis/json_to_csv/_raw_data/hot-bitcoin1427836487.05.json')
	print local_obj.get_file_path()
	pprint(local_obj.read_json())

if __name__ == "__main__":
	main()
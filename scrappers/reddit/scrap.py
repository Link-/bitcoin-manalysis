#!/usr/bin/python
# 
# Python Submissions Scrapper
# for the purposes of the bitcoin
# trend analysis excercise
# 
# @version: 0.0.1
# @dependencies: requests
#
# run: 
# $: python scrap.py
#
# Note: This is hacked code 
# in a rush so don't judge

import requests
import json
import time
import pprint

DATA_DIR = '/Users/bassemd/Projects/bitcoin-manalysis/scrappers/reddit/_raw_data/'
PARSE_CONF = {'subreddit': 'http://www.reddit.com/r/bitcoin/',
							'flair': 'hot',
							'format': 'json',
							'timeout': 10,
							'depth': 10,
							'sleep_thresh': 3}


def request_data(url, after=''):
	# If next cursor key exists
	# Add it to the url
	if after:
		suffix = '?after=%s' % after
		url = url + suffix	
	# Define the user-agent
	headers = {'user-agent': 'Bitcoin-analysis:v0.0.1 (by /u/Link-)'}
	# Intialize the request + timeout
	r = requests.get(url, headers=headers, timeout=PARSE_CONF['timeout'])
	# Debugging : Print status code
	print r.status_code
	# Return content
	return r.content

def dump_info_file(content):
	# Define the filename
	curr_filename = '%shot-bitcoin-%s.%s' % (DATA_DIR, str(time.time()), 'json')
	# Write conent to file
	with open(curr_filename, 'wb') as feed:
		feed.write(content)

def get_data(url, after=''):
	# Get content
	ir_content = request_data(url, after)
	# Dump data into a file
	dump_info_file(ir_content)
	# jsonify
	json_content = json.loads(ir_content)
	# Get the after cursor key
	after_flag = json_content['data']['after']
	# Return next cursor key
	return after_flag

def main():
	# Initial url
	url = '%s%s.%s' % (PARSE_CONF['subreddit'], \
										 PARSE_CONF['flair'], \
										 PARSE_CONF['format'])
	# Initial data request
	after_flag = get_data(url)
	# Depth
	cur_depth = PARSE_CONF['depth']
	# Debuggin purposes
	print "DEPTH %d : %s" % (cur_depth, after_flag)
	# Loop
	while (after_flag and cur_depth > 0):
		print "SLEEPING %d seconds" % (PARSE_CONF['sleep_thresh'])
		# Wait between each request and the
		# next so that we don't
		# banned
		time.sleep(PARSE_CONF['sleep_thresh'])
		# Store the new next cursor key
		after_flag = get_data(url, after_flag)
		# Debuggin 
		print "DEPTH %d : %s" % (cur_depth, after_flag)
		# Decrement the depth cursor
		cur_depth = cur_depth - 1


if __name__ == "__main__":
	main()